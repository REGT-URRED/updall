# -*- coding: utf-8 -*-
"""
project_context.py - Contexto del proyecto para Strands Agent.

Este archivo contiene el contexto completo del proyecto, generado por ContextBase,
para que un agente Strands pueda trabajar organizado, sincronizado y sin perder
el hilo entre sesiones. Importalo directamente en tu proyecto Strands.

Generado por: ContextBase CLI
Fecha de generacion: 2026-11-18T15:51:58.412Z
Directorio del proyecto: D:/PROCESO/updall
"""

# ============================================================================
# 1. IDENTIFICACION DEL PROYECTO
# ============================================================================
PROJECT_NAME = 'updall'
PROJECT_DIR = 'D:\\PROCESO\\updall'
PROJECT_VERSION = '0.1.0'
PROJECT_TYPE = 'Generic'
PROJECT_DESCRIPTION = 'Actualizador global de la integración de **ContextBase** para agentes de código.'
FRAMEWORKS = []
LANGUAGES = {'Markdown': 23, 'JavaScript': 1, 'JSON': 14, 'Python': 4, 'PowerShell': 1}
GENERATED_AT = '2026-11-18T15:51:58.412Z'

# ============================================================================
# 2. TAREAS PENDIENTES Y COMPLETADAS
# ============================================================================
# PENDING_TASKS: lista de diccionarios con id, descripcion, estado, prioridad y fecha.
PENDING_TASKS = [{'id': 'T-001', 'descripcion': 'Actualizador global de ContextBase (update-global.ps1)', 'estado': 'pendiente', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.412Z'}, {'id': 'T-002', 'descripcion': 'Creación del actualizador global de ContextBase (update-global.ps1)', 'estado': 'pendiente', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.412Z'}, {'id': 'T-003', 'descripcion': 'Validar cobertura de pruebas funcionales y unitarias', 'estado': 'pendiente', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.412Z'}, {'id': 'T-004', 'descripcion': 'Revisar optimizaciones de rendimiento y seguridad', 'estado': 'pendiente', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.412Z'}, {'id': 'T-005', 'descripcion': 'Preparar empaquetado o despliegue a producción', 'estado': 'pendiente', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.412Z'}]
# COMPLETED_TASKS: lista de diccionarios de tareas ya realizadas.
COMPLETED_TASKS = [{'id': 'T-006', 'descripcion': 'Creación de carpeta de memoria persistente `contextbase/`', 'estado': 'completada', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.412Z'}, {'id': 'T-007', 'descripcion': 'Generación de documento estructurado `fundamentos.md`', 'estado': 'completada', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.412Z'}, {'id': 'T-008', 'descripcion': 'Creación de bitácora histórica `changelog.md`', 'estado': 'completada', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.412Z'}, {'id': 'T-009', 'descripcion': 'Configuración de lista de tareas visual de alto contraste `tasklist.md`', 'estado': 'completada', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.412Z'}, {'id': 'T-010', 'descripcion': 'Inyección de directivas y reglas críticas para agentes de código (`AGENTS.md`, `CLAUDE.md`, `.cursorrules`)', 'estado': 'completada', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.412Z'}, {'id': 'T-011', 'descripcion': 'Escaneo y análisis retroactivo de los archivos del proyecto (`updall`)', 'estado': 'completada', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.412Z'}, {'id': 'T-012', 'descripcion': 'Creación del actualizador global de ContextBase (`update-global.ps1`)', 'estado': 'completada', 'prioridad': 'media', 'fecha': '2026-11-18T15:51:58.412Z'}]
TOTAL_TASKS = len(PENDING_TASKS) + len(COMPLETED_TASKS)

# ============================================================================
# 3. SEGURIDAD Y VULNERABILIDADES
# ============================================================================
# SECURITY_ISSUES: vulnerabilidades critical y high detectadas en componentes.
SECURITY_ISSUES = []
SECURITY_CRITICAL_COUNT = 0
SECURITY_HIGH_COUNT = 0
SECURITY_HAS_ISSUES = False

# ============================================================================
# 4. COMPONENTES Y DEPENDENCIAS
# ============================================================================
# COMPONENTS: inventario de dependencias del proyecto.
COMPONENTS = []
DEPENDENCIES = []
DEV_DEPENDENCIES = []
SCRIPTS = {}

# ============================================================================
# 5. ARCHIVOS DE REGLAS Y VERSIONES
# ============================================================================
# RULE_FILES: mapa de archivos de regla con su version CONTEXTBASE detectada.
RULE_FILES = {'AGENTS.md': '1.5.0', 'CLAUDE.md': '1.5.0', '.cursorrules': '1.5.0', '.windsurfrules': '1.5.0', '.agents/rules/contextbase.md': '1.5.0'}
RULE_FILES_PRESENT = ['AGENTS.md', 'CLAUDE.md', '.cursorrules', '.windsurfrules', '.agents/rules/contextbase.md']

# ============================================================================
# 6. ESTADO DEL GUARDIA DE ARCHIVOS BASE
# ============================================================================
# GUARD_STATUS: ok o drift.
GUARD_STATUS = 'ok'
# GUARD_DRIFTS: lista de archivos con deriva (file, kind).
GUARD_DRIFTS = []
GUARD_HAS_DRIFT = False

# ============================================================================
# 7. SIGUIENTE ACCION RECOMENDADA
# ============================================================================
# NEXT_ACTION: accion recomendada para la siguiente sesion del agente.
NEXT_ACTION = 'Continuar con la tarea pendiente: Actualizador global de ContextBase (update-global.ps1)'

# ============================================================================
# 8. GIT HISTORY Y TODOS
# ============================================================================
GIT_HISTORY = ['2026-11-18 | Add global ContextBase updater and full agent configuration', '2026-11-18 | first commit']
# TODOS: tareas detectadas en codigo (TODO, FIXME, HACK, BUG).
TODOS = []

# ============================================================================
# 9. FUNCIONES DE ACCESO RAPIDO
# ============================================================================
def get_pending_tasks():
    '''Retorna la lista de tareas pendientes.'''
    return PENDING_TASKS

def get_completed_tasks():
    '''Retorna la lista de tareas completadas.'''
    return COMPLETED_TASKS

def get_security_issues():
    '''Retorna los problemas de seguridad detectados.'''
    return SECURITY_ISSUES

def get_next_action():
    '''Retorna la siguiente accion recomendada.'''
    return NEXT_ACTION

def has_critical_security_issues():
    '''True si hay vulnerabilidades critical sin corregir.'''
    return SECURITY_CRITICAL_COUNT > 0

def has_guard_drift():
    '''True si el guardia detecta deriva en archivos base.'''
    return GUARD_HAS_DRIFT

if __name__ == "__main__":
    print("PROJECT:", PROJECT_NAME)
    print("VERSION:", PROJECT_VERSION)
    print("PENDING_TASKS:", len(PENDING_TASKS))
    print("COMPLETED_TASKS:", len(COMPLETED_TASKS))
    print("SECURITY_CRITICAL:", SECURITY_CRITICAL_COUNT)
    print("SECURITY_HIGH:", SECURITY_HIGH_COUNT)
    print("GUARD_STATUS:", GUARD_STATUS)
    print("NEXT_ACTION:", NEXT_ACTION)

