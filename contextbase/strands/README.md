# Contexto Strands Agent

Directorio generado por ContextBase para integrar Strands Agent (Python) con el proyecto.

## Archivos generados

- `context.json` - Estado estructurado del proyecto en JSON.
- `project_context.py` - Variables y constantes del contexto para importar en Strands.
- `strands_config.py` - Configuracion de agente, herramientas, enjambre y hooks.
- `tasks.py` - Lista de tareas pendientes como estructuras de Python.
- `strands_runner.py` - Ejecutable que arma el prompt, ejecuta Strands si esta disponible y escala al humano solo por urgencia.
- `README.md` - Esta documentacion.

## Uso con Strands Agent

Importa el contexto en tu agente Strands:

```python
from project_context import PROJECT_NAME, PROJECT_DIR, PENDING_TASKS, NEXT_ACTION
from strands_config import AGENT_CONFIG, TOOLS_CONFIG, HOOKS_CONFIG
from tasks import get_pending_tasks, mark_done
```

## Ejecucion autonoma

Ejecuta el runner desde este directorio:

```bash
python strands_runner.py
```

El runner escala al humano solo cuando hay vulnerabilidades critical/high o deriva detectada por el guardia (salida 2). Si el SDK de Strands no esta instalado, muestra el prompt completo en modo seco (salida 0).

El contexto se regenera automaticamente despues de cada `log`, `task`, `audit` o `sync`; no requiere un comando manual.

## Flujo de trabajo recomendado

1. Al iniciar una sesion, carga `context.json` y `project_context.py`.
2. Revisa `NEXT_ACTION` para saber que hacer a continuacion.
3. Ejecuta las tareas pendientes usando `get_pending_tasks()`.
4. Al completar una tarea, usa `mark_done(task_id)`.
5. Al cerrar el cambio, registra el avance y el contexto se regenera solo.

## Proyecto
- Nombre: updall
- Directorio: D:\PROCESO\updall
- Version: 0.1.0
- Pendientes: 5
- Completadas: 7
- Seguridad critical: 0
- Seguridad high: 0
- Guardia: ok

Generado el 2026-11-18T15:48:03.561Z por ContextBase CLI.
