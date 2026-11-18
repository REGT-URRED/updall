# updall

Actualizador global de la integración de **ContextBase** para agentes de código.

## Problema que resuelve

Cuando ContextBase actualiza sus reglas, skills o configuración, hay que repetir el proceso en cada agente (OpenCode, Kilo Code, Claude Code, Antigravity/Gemini, `.agents`). `updall` concentra ese ciclo en **un solo comando** y solo actúa sobre los agentes que existen en la máquina, así que funciona igual en equipos con muchas herramientas instaladas que en equipos con pocas.

## Requisitos

- **Node.js** (runtime del CLI de ContextBase).
- **ContextBase CLI v1.5.0 o superior**: `npm install -g contextbase`.
- **PowerShell 5+ o PowerShell 7+**.

En Windows, si el equipo bloquea scripts locales, habilitar una vez:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Uso

Clonar el repositorio y ejecutar desde su raíz:

```powershell
.\update-global.ps1
```

### Opciones

| Parámetro | Descripción |
| --- | --- |
| `-RepoRoot <ruta>` | Carpeta del proyecto contextbase. Por defecto, la carpeta del script. |
| `-ContextBaseBin <ruta>` | Ruta alternativa a `contextbase.js`. Por defecto, la instalación global de npm. |
| `-DryRun` | Muestra los comandos sin ejecutarlos. |

Ejemplo con ruta explícita:

```powershell
.\update-global.ps1 -RepoRoot "D:\PROCESO\updall"
```

## Ciclo de actualización

El script orquesta cinco comandos del CLI de ContextBase:

1. `contextbase doctor --fix` — diagnóstico y reparación automática de la instalación global.
2. `contextbase install-skill` — instala `contextbase` y `contextbase-egm` en los homes de agentes detectados y registra el MCP.
3. `contextbase sync` — reinyecta las reglas de agente (`AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.windsurfrules`, reglas por agente) y sincroniza el bloque técnico de `contextbase/fundamentos.md`.
4. `contextbase guard` — verifica la integridad de los archivos base y repara deriva.
5. `contextbase status --check` — chequeo final de estado; el script termina con código `1` si algo falló o hay deriva.

## Agentes cubiertos

El alcance lo define el propio CLI de ContextBase: **OpenCode**, **Kilo Code**, **Claude Code**, **Antigravity/Gemini CLI** y el home universal **`.agents`**. Un agente no instalado no produce error: simplemente se omite.

> Nota: `pi` y `omp` pueden estar instalados en la máquina, pero hoy no están dentro del registry de ContextBase, por lo que este actualizador aún no los cubre.

## Estructura del repositorio

| Ruta | Contenido |
| --- | --- |
| `update-global.ps1` | Actualizador global (punto de entrada). |
| `contextbase/` | Memoria técnica persistente, bitácora, tareas, snapshots y veredicto EGM. |
| `.opencode/`, `.kilo/`, `.kilocode/`, `.agents/` | Reglas, skills y MCP por agente. |
| `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.windsurfrules` | Reglas compartidas para agentes de código. |
| `opencode.json`, `kilo.json`, `.mcp.json` | Configuración local de MCP y permisos. |

## Autor

**REGT-URRED** — U19211826@utp.edu.pe
