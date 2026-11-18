# -*- coding: utf-8 -*-
"""
strands_config.py - Configuracion para Strands Agent.

Configuracion de agentes, herramientas, enjambre y hooks para Strands.
Generado por ContextBase CLI el 2026-11-18T15:51:58.413Z.
"""

# ============================================================================
# AGENT_CONFIG
# ============================================================================
# Configuracion del agente Strands: modelo, temperatura, max_tokens.
AGENT_CONFIG = {'model': 'claude-3-5-sonnet-20241022', 'temperature': 0.2, 'max_tokens': 4096, 'system_prompt': 'Eres un agente Strands que trabaja sobre el proyecto contextbase. Usa project_context.py para mantener el contexto entre sesiones.', 'language': 'es'}

# ============================================================================
# TOOLS_CONFIG
# ============================================================================
# Herramientas disponibles para el agente.
TOOLS_CONFIG = {'available': [{'name': 'read_file', 'description': 'Leer un archivo del proyecto'}, {'name': 'write_file', 'description': 'Escribir un archivo del proyecto'}, {'name': 'list_directory', 'description': 'Listar contenido de un directorio'}, {'name': 'run_command', 'description': 'Ejecutar un comando de terminal'}, {'name': 'search_code', 'description': 'Buscar patrones en el codigo'}], 'max_concurrent': 5, 'timeout_ms': 30000}

# ============================================================================
# SWARM_CONFIG
# ============================================================================
# Configuracion de enjambre si se usa trabajo distribuido.
SWARM_CONFIG = {'enabled': False, 'max_workers': 3, 'strategy': 'sequential', 'shared_context_file': 'contextbase/strands/context.json'}

# ============================================================================
# HOOKS_CONFIG
# ============================================================================
# Hooks pre/post ejecucion y manejo de errores.
HOOKS_CONFIG = {'pre_execution': [{'hook': 'load_context', 'description': 'Cargar context.json y project_context.py antes de ejecutar'}, {'hook': 'check_guard', 'description': 'Verificar que no hay deriva en archivos base'}], 'post_execution': [{'hook': 'save_context', 'description': 'Guardar estado actualizado tras la ejecucion'}, {'hook': 'log_action', 'description': 'Registrar la accion ejecutada en tasklist.md'}], 'on_error': [{'hook': 'report_error', 'description': 'Reportar error y volver al estado ultimo valido'}]}

# ============================================================================
# FUNCIONES DE ACCESO
# ============================================================================
def get_agent_config():
    '''Retorna la configuracion del agente.'''
    return AGENT_CONFIG

def get_tools_config():
    '''Retorna la configuracion de herramientas.'''
    return TOOLS_CONFIG

def get_swarm_config():
    '''Retorna la configuracion de enjambre.'''
    return SWARM_CONFIG

def get_hooks_config():
    '''Retorna la configuracion de hooks.'''
    return HOOKS_CONFIG

if __name__ == "__main__":
    print("AGENT_CONFIG:", AGENT_CONFIG)
    print("TOOLS_CONFIG:", TOOLS_CONFIG)
    print("SWARM_CONFIG:", SWARM_CONFIG)
    print("HOOKS_CONFIG:", HOOKS_CONFIG)

