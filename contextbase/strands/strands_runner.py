# -*- coding: utf-8 -*-
"""
strands_runner.py - Ejecutable listo para Strands Agent.

Carga el contexto generado por ContextBase y prepara una sesion autonoma.
Escala al humano solo cuando existe una urgencia real: vulnerabilidades
critical/high o deriva detectada por el guardia de archivos base.
"""

from project_context import (
    PROJECT_NAME,
    PENDING_TASKS,
    NEXT_ACTION,
    SECURITY_ISSUES,
    SECURITY_HAS_ISSUES,
    GUARD_HAS_DRIFT,
    TOTAL_TASKS,
)
from strands_config import AGENT_CONFIG

ESCALATE_TO_HUMAN = SECURITY_HAS_ISSUES or GUARD_HAS_DRIFT

SYSTEM_PROMPT = (
    "Eres un agente Strands que trabaja de forma autonoma sobre el proyecto "
    + str(PROJECT_NAME)
    + ". Usa el contexto de ContextBase, respeta las tareas pendientes, "
    + "registra cada cambio y no inventes resultados."
)


def build_prompt():
    """Arma el prompt en espanol con el estado actual del proyecto."""
    lines = []
    lines.append("Proyecto: " + str(PROJECT_NAME))
    lines.append("Tareas totales: " + str(TOTAL_TASKS))
    lines.append("")
    lines.append("Tareas pendientes (maximo 10):")
    if PENDING_TASKS:
        for task in PENDING_TASKS[:10]:
            if isinstance(task, dict):
                task_id = task.get("id", "")
                desc = task.get("descripcion") or task.get("description") or task
                lines.append("- [" + str(task_id) + "] " + str(desc))
            else:
                lines.append("- " + str(task))
    else:
        lines.append("- Sin tareas pendientes registradas.")
    lines.append("")
    lines.append("Siguiente accion recomendada: " + str(NEXT_ACTION))
    if SECURITY_ISSUES:
        lines.append("")
        lines.append("Advertencia de seguridad:")
        for issue in SECURITY_ISSUES[:5]:
            if isinstance(issue, dict):
                sev = issue.get("severidad", "?")
                count = issue.get("cantidad", "?")
                desc = issue.get("descripcion", "")
                lines.append("- " + str(sev) + " (" + str(count) + "): " + str(desc))
            else:
                lines.append("- " + str(issue))
    if GUARD_HAS_DRIFT:
        lines.append("")
        lines.append("Advertencia: el guardia detecto deriva en archivos base; se requiere revision humana.")
    return "\n".join(lines)


def main():
    prompt = build_prompt()
    if ESCALATE_TO_HUMAN:
        print("[ESCALAR AL HUMANO] Seguridad critical/high o deriva del guardia detectada.")
        if SECURITY_ISSUES:
            print("Motivo: " + str(SECURITY_ISSUES))
        if GUARD_HAS_DRIFT:
            print("Motivo: deriva detectada en archivos base por el guardia.")
        print("")
        print(prompt)
        return 2
    try:
        from strands import Agent
    except ImportError:
        print(prompt)
        print("")
        print("[MODO SECO] SDK de Strands no instalado; se mostro el prompt completo.")
        print("ContextBase lo gestiona solo: 'contextbase strands sdk --install' (o pip install strands-agents).")
        return 0
    try:
        agent = Agent(model=AGENT_CONFIG.get("model"), system_prompt=SYSTEM_PROMPT)
        result = agent(prompt)
    except Exception as err:
        print(prompt)
        print("")
        print("[MODO DEGRADADO] SDK de Strands disponible pero el proveedor de modelo no respondio: " + type(err).__name__ + ": " + str(err)[:300])
        print("Se mostro el prompt completo. Configura las credenciales del proveedor (p.ej. AWS para Bedrock) o fija el modelo con CONTEXTBASE_STRANDS_MODEL.")
        return 3
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

