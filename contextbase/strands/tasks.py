# -*- coding: utf-8 -*-
"""
tasks.py - Lista de tareas pendientes como estructuras de Python.

Cada tarea es un diccionario con id, descripcion, estado, prioridad y fecha.
Generado por ContextBase CLI.
"""

# ============================================================================
# TAREAS
# ============================================================================
# Lista de diccionarios de tareas.
TASKS = [{'id': 'T-001', 'descripcion': 'Actualizador global de ContextBase (update-global.ps1)', 'estado': 'pendiente', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.414Z'}, {'id': 'T-002', 'descripcion': 'Creación del actualizador global de ContextBase (update-global.ps1)', 'estado': 'pendiente', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.414Z'}, {'id': 'T-003', 'descripcion': 'Validar cobertura de pruebas funcionales y unitarias', 'estado': 'pendiente', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.414Z'}, {'id': 'T-004', 'descripcion': 'Revisar optimizaciones de rendimiento y seguridad', 'estado': 'pendiente', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.414Z'}, {'id': 'T-005', 'descripcion': 'Preparar empaquetado o despliegue a producción', 'estado': 'pendiente', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.414Z'}, {'id': 'T-006', 'descripcion': 'Creación de carpeta de memoria persistente `contextbase/`', 'estado': 'completada', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.414Z'}, {'id': 'T-007', 'descripcion': 'Generación de documento estructurado `fundamentos.md`', 'estado': 'completada', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.414Z'}, {'id': 'T-008', 'descripcion': 'Creación de bitácora histórica `changelog.md`', 'estado': 'completada', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.414Z'}, {'id': 'T-009', 'descripcion': 'Configuración de lista de tareas visual de alto contraste `tasklist.md`', 'estado': 'completada', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.414Z'}, {'id': 'T-010', 'descripcion': 'Inyección de directivas y reglas críticas para agentes de código (`AGENTS.md`, `CLAUDE.md`, `.cursorrules`)', 'estado': 'completada', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.414Z'}, {'id': 'T-011', 'descripcion': 'Escaneo y análisis retroactivo de los archivos del proyecto (`updall`)', 'estado': 'completada', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.414Z'}, {'id': 'T-012', 'descripcion': 'Creación del actualizador global de ContextBase (`update-global.ps1`)', 'estado': 'completada', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.414Z'}]

PENDING_TASKS = [t for t in TASKS if t.get("estado") == "pendiente"]
COMPLETED_TASKS = [t for t in TASKS if t.get("estado") == "completada"]

# ============================================================================
# FUNCIONES DE ACCESO
# ============================================================================
def get_tasks():
    '''Retorna todas las tareas.'''
    return TASKS

def get_pending_tasks():
    '''Retorna solo las tareas pendientes.'''
    return PENDING_TASKS

def get_completed_tasks():
    '''Retorna solo las tareas completadas.'''
    return COMPLETED_TASKS

def add_task(descripcion, prioridad="media"):
    """Agrega una nueva tarea pendiente."""
    import datetime
    new_id = "T-" + str(len(TASKS) + 1).zfill(3)
    task = {
        "id": new_id,
        "descripcion": descripcion,
        "estado": "pendiente",
        "prioridad": prioridad,
        "fecha": datetime.datetime.utcnow().isoformat() + "Z"
    }
    TASKS.append(task)
    return task

def mark_done(task_id):
    """Marca una tarea como completada."""
    for t in TASKS:
        if t.get("id") == task_id:
            t["estado"] = "completada"
            return t
    return None

if __name__ == "__main__":
    print("Total tareas:", len(TASKS))
    print("Pendientes:", len(PENDING_TASKS))
    print("Completadas:", len(COMPLETED_TASKS))
    for t in PENDING_TASKS:
        print(t["id"], "-", t["descripcion"])

