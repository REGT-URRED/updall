// Generado por ContextBase - Plugin de automatizacion de ciclo de vida y Telarana para OpenCode y Kilo Code
import { execFile, execFileSync, spawn } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';

const DEFAULT_NODE_BIN = "C:/Program Files/nodejs/node.exe";
const DEFAULT_CB_BIN = "C:/Users/TOOR/AppData/Roaming/npm/node_modules/contextbase/bin/contextbase.js";

// El host puede cargar el plugin DOS veces (global y proyecto) en el mismo proceso.
// Solo la primera instancia registra hooks: la segunda devuelve un plugin vacio para
// no duplicar tareas, hooks de ciclo de vida ni inyecciones del digest.
const CONTEXTBASE_PLUGIN_KEY = "__contextbaseAutoPluginActive";
function claimPluginSlot() {
  try {
    if (globalThis[CONTEXTBASE_PLUGIN_KEY]) return false;
    globalThis[CONTEXTBASE_PLUGIN_KEY] = true;
    return true;
  } catch {
    return true;
  }
}

function resolveWorkdir(ctx) {
  return (ctx && (ctx.directory || ctx.worktree)) || process.cwd();
}

function resolveCbCommand(cwd) {
  const nodeBin = fs.existsSync(DEFAULT_NODE_BIN) ? DEFAULT_NODE_BIN : (process.execPath || "node");
  const globalNpmBin = process.env.APPDATA ? path.join(process.env.APPDATA, "npm", "node_modules", "contextbase", "bin", "contextbase.js") : "";
  const candidates = [
    DEFAULT_CB_BIN,
    globalNpmBin,
    path.join(cwd, "bin", "contextbase.js"),
    path.join(cwd, "..", "..", "bin", "contextbase.js"),
    path.join(cwd, "node_modules", "contextbase", "bin", "contextbase.js")
  ];
  for (const cand of candidates) {
    if (cand && fs.existsSync(cand)) return { bin: nodeBin, prefix: [cand] };
  }
  // Sin binario de ContextBase no inventamos un comando: en Windows fallaba con ENOENT/EINVAL y abortaba el host.
  return null;
}

function readSpiderContext(cwd) {
  try {
    const p = path.join(cwd, "contextbase", ".spider-context.json");
    if (!fs.existsSync(p)) return null;
    return JSON.parse(fs.readFileSync(p, "utf8"));
  } catch {
    return null;
  }
}

function runSyncHook(event, cwd, extra = []) {
  try {
    const resolved = resolveCbCommand(cwd);
    if (!resolved) return "";
    return execFileSync(resolved.bin, [...resolved.prefix, "hook-run", event, ...extra], {
      cwd,
      encoding: "utf8",
      timeout: 8000,
      windowsHide: true,
      stdio: ["ignore", "pipe", "ignore"]
    }).trim();
  } catch {
    return "";
  }
}

function runAsyncHook(event, cwd, extra = []) {
  try {
    const resolved = resolveCbCommand(cwd);
    if (!resolved) return;
    const child = spawn(resolved.bin, [...resolved.prefix, "hook-run", event, ...extra], {
      cwd,
      detached: true,
      windowsHide: true,
      stdio: "ignore"
    });
    child.on("error", () => {});
    child.unref();
  } catch {}
}

const MUTATING_TOOLS = new Set([
  "edit", "write", "patch", "apply_patch", "multi_edit", "multiedit",
  "create_file", "write_to_file", "replace_in_file", "bash", "todowrite"
]);

export const ContextBaseAutoPlugin = async (ctx = {}) => {
  if (!claimPluginSlot()) return {};
  const workDir = resolveWorkdir(ctx);
  const touchedFiles = new Set();
  const spiderMeta = readSpiderContext(workDir);
  let digestCache = "";
  let lastDigestAt = 0;

  function getDigest() {
    const now = Date.now();
    if (!digestCache || (now - lastDigestAt) > 12000) {
      const out = runSyncHook("session-start", workDir);
      if (out) {
        digestCache = out;
        lastDigestAt = now;
      }
    }
    return digestCache;
  }

  getDigest();

  return {
    "experimental.chat.system.transform": async (_input, output) => {
      try {
        const digest = getDigest();
        if (!digest || !output) return;
        const marker = "<!-- CONTEXTBASE:LIVE_DIGEST -->";
        const block = `${marker}\n${digest}\n<!-- /CONTEXTBASE:LIVE_DIGEST -->`;
        const END = "<!-- /CONTEXTBASE:LIVE_DIGEST -->";
        if (Array.isArray(output.system)) {
          const idx = output.system.findIndex(s => typeof s === "string" && s.includes(marker));
          if (idx >= 0) {
            const current = output.system[idx];
            const end = current.indexOf(END);
            const head = end >= 0 ? current.slice(0, current.indexOf(marker)) : current;
            const tail = end >= 0 ? current.slice(end + END.length) : "";
            output.system[idx] = head + block + tail;
          } else {
            output.system.push(block);
          }
        } else if (typeof output.system === "string") {
          const end = output.system.indexOf(END);
          if (output.system.includes(marker) && end >= 0) {
            const head = output.system.slice(0, output.system.indexOf(marker));
            const tail = output.system.slice(end + END.length);
            output.system = head + block + tail;
          } else if (!output.system.includes(marker)) {
            output.system = `${output.system}\n\n${block}`;
          }
        } else {
          output.system = block;
        }
      } catch {}
    },
    "chat.message": async () => {
      try { getDigest(); } catch {}
    },
    "tool.execute.before": async (input) => {
      try {
        if (!spiderMeta || !Array.isArray(spiderMeta.forbiddenFiles)) return;
        const toolName = String((input && input.tool) || "").toLowerCase();
        if (!MUTATING_TOOLS.has(toolName) || toolName === "bash" || toolName === "todowrite") return;
        const args = (input && input.args) || {};
        const rawTarget = args.filePath || args.path || args.file || "";
        if (!rawTarget) return;
        const relTarget = path.isAbsolute(rawTarget) ? path.relative(workDir, rawTarget) : String(rawTarget);
        const normTarget = path.resolve(workDir, relTarget).toLowerCase();
        const forbidden = spiderMeta.forbiddenFiles.map(f => path.resolve(workDir, String(f)).toLowerCase());
        if (forbidden.includes(normTarget)) {
          throw new Error(`[ContextBase Telaraña] Aislamiento de hilo activo: el archivo "${relTarget}" pertenece a otra Araña. Modifica solo tus archivos asignados: ${(spiderMeta.assignedFiles || []).join(", ")}`);
        }
      } catch (err) {
        if (err && String(err.message || "").includes("[ContextBase Telaraña]")) throw err;
      }
    },
    "tool.execute.after": async (input, output) => {
      try {
        const toolName = String((input && input.tool) || "").toLowerCase();
        if (!MUTATING_TOOLS.has(toolName) && !toolName.startsWith("contextbase_")) return;
        const args = (input && input.args) || (output && output.args) || {};
        const target = args.filePath || args.path || args.file || (output && output.metadata && output.metadata.filePath) || "";
        if (target) touchedFiles.add(String(target));
        else if (toolName !== "bash") touchedFiles.add(toolName);
        if (toolName === "todowrite" && Array.isArray(args.todos)) {
          for (const t of args.todos) {
            const content = t && (t.content || t.text || t.description);
            const status = t && t.status;
            if (content && status === "completed") runAsyncHook("task-done", workDir, [String(content)]);
            else if (content && (status === "pending" || status === "in_progress")) runAsyncHook("task-add", workDir, [String(content)]);
          }
        }
        lastDigestAt = 0;
      } catch {}
    },
    event: async ({ event }) => {
      try {
        const type = event && event.type;
        if (type === "session.created") {
          getDigest();
        } else if (type === "file.edited" || type === "file.watcher.updated") {
          const p = (event.data && event.data.path) || (event.properties && event.properties.file);
          if (p) touchedFiles.add(String(p));
        } else if (type === "session.idle") {
          if (touchedFiles.size > 0) {
            const list = Array.from(touchedFiles).slice(0, 15);
            touchedFiles.clear();
            runAsyncHook("session-stop", workDir, list);
            lastDigestAt = 0;
          }
        }
      } catch {}
    },
    stop: async () => {
      try {
        if (touchedFiles.size > 0) {
          const list = Array.from(touchedFiles).slice(0, 15);
          touchedFiles.clear();
          runSyncHook("session-stop", workDir, list);
        }
      } catch {}
    }
  };
};

// OpenCode V2 (Promise API): setup(ctx) registra hooks via ctx. V1 usa el export nombrado.
async function setupContextBaseAuto(ctx = {}) {
  try {
    if (!claimPluginSlot()) return;
    const hasSessionHook = ctx && ctx.session && typeof ctx.session.hook === "function";
    const hasToolHook = ctx && ctx.tool && typeof ctx.tool.hook === "function";
    if (!hasSessionHook && !hasToolHook) return;

    const workDir = (ctx.location && ctx.location.directory) || ctx.directory || ctx.worktree || process.cwd();
    const spiderMeta = readSpiderContext(workDir);
    const touchedFiles = new Set();
    const registrations = [];
    let digest = "";
    let digestAt = 0;
    let refreshing = null;

    const runHookPromise = (event, extra = []) => new Promise((resolve) => {
      try {
        const resolved = resolveCbCommand(workDir);
        if (!resolved) return resolve("");
        execFile(resolved.bin, [...resolved.prefix, "hook-run", event, ...extra], {
          cwd: workDir, encoding: "utf8", timeout: 8000, windowsHide: true, maxBuffer: 1048576
        }, (err, stdout) => resolve(err ? "" : String(stdout || "").trim()));
      } catch { resolve(""); }
    });

    const refreshDigest = (force = false) => {
      const now = Date.now();
      if (!force && digest && now - digestAt < 60000) return Promise.resolve();
      if (refreshing) return refreshing;
      refreshing = runHookPromise("session-start")
        .then((out) => { if (out) { digest = out; digestAt = Date.now(); } })
        .catch(() => {})
        .finally(() => { refreshing = null; });
      return refreshing;
    };

    const pushSystem = (event) => {
      if (!event || !Array.isArray(event.system) || !digest) return;
      const marker = "<!-- CONTEXTBASE:LIVE_DIGEST -->";
      const endMarker = "<!-- /CONTEXTBASE:LIVE_DIGEST -->";
      const block = `${marker}\n${digest}\n${endMarker}`;
      const existing = event.system.find((part) => part && typeof part.text === "string" && part.text.includes(marker));
      if (!existing) { event.system.push({ type: "text", text: block }); return; }
      const current = String(existing.text);
      const start = current.indexOf(marker);
      const end = current.indexOf(endMarker);
      const tail = end >= 0 ? current.slice(end + endMarker.length) : "";
      existing.text = current.slice(0, start) + block + tail;
    };

    const toolInput = (event) => (event && (event.input || event.args)) || {};
    const toolTarget = (input) => (input && typeof input === "object" && (input.filePath || input.path || input.file)) || "";

    const checkIsolation = (event) => {
      if (!spiderMeta || !Array.isArray(spiderMeta.forbiddenFiles)) return;
      const toolName = String((event && event.tool) || "").toLowerCase();
      if (!MUTATING_TOOLS.has(toolName) || toolName === "bash" || toolName === "todowrite") return;
      const rawTarget = toolTarget(toolInput(event));
      if (!rawTarget) return;
      const relTarget = path.isAbsolute(rawTarget) ? path.relative(workDir, rawTarget) : String(rawTarget);
      const normTarget = path.resolve(workDir, relTarget).toLowerCase();
      const forbidden = spiderMeta.forbiddenFiles.map((f) => path.resolve(workDir, String(f)).toLowerCase());
      if (forbidden.includes(normTarget)) {
        throw new Error(`[ContextBase Telarana] Aislamiento de hilo activo: el archivo "${relTarget}" pertenece a otra Arana. Modifica solo tus archivos asignados: ${(spiderMeta.assignedFiles || []).join(", ")}`);
      }
    };

    const trackResult = (event) => {
      const toolName = String((event && event.tool) || "").toLowerCase();
      if (!MUTATING_TOOLS.has(toolName) && !toolName.startsWith("contextbase_")) return;
      const input = toolInput(event);
      const target = toolTarget(input) || (event && event.result && event.result.metadata && event.result.metadata.filePath) || "";
      if (target) touchedFiles.add(String(target));
      if (toolName === "todowrite" && Array.isArray(input.todos)) {
        for (const todo of input.todos) {
          const content = todo && (todo.content || todo.text || todo.description);
          if (!content) continue;
          if (todo.status === "completed") runAsyncHook("task-done", workDir, [String(content)]);
          else if (todo.status === "pending" || todo.status === "in_progress") runAsyncHook("task-add", workDir, [String(content)]);
        }
      }
      digestAt = 0;
    };

    void refreshDigest(true);

    if (hasSessionHook) {
      try {
        const reg = await ctx.session.hook("context", (event) => { try { pushSystem(event); } catch {} });
        if (reg) registrations.push(reg);
      } catch {}
    }

    if (hasToolHook) {
      try {
        const reg = await ctx.tool.hook("execute.before", (event) => {
          try { checkIsolation(event); } catch (err) {
            if (err && String(err.message || "").includes("[ContextBase Telarana]")) throw err;
          }
        });
        if (reg) registrations.push(reg);
      } catch {}
      try {
        const reg = await ctx.tool.hook("execute.after", (event) => { try { trackResult(event); } catch {} });
        if (reg) registrations.push(reg);
      } catch {}
    }

    const timer = setInterval(() => {
      void runHookPromise("web-pulse");
      void refreshDigest(true);
    }, 60000);
    if (typeof timer.unref === "function") timer.unref();

    return async () => {
      clearInterval(timer);
      if (touchedFiles.size > 0) {
        const list = Array.from(touchedFiles).slice(0, 15);
        touchedFiles.clear();
        await runHookPromise("session-stop", list);
      }
      for (const registration of registrations) {
        try { await registration.dispose?.(); } catch {}
      }
    };
  } catch {
    return;
  }
}

// Contrato OpenCode v2: default export objeto con id + setup (API Promise).
// No incluir effect: si existe, el runtime lo prefiere y la activacion del
// plugin queda colgada esperando hooks de ctx. setup es el contrato soportado.
export default {
  id: "contextbase-auto",
  server: ContextBaseAutoPlugin,
  setup: setupContextBaseAuto
};
