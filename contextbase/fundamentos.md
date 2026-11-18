# Fundamentos del Proyecto: updall

## 1. Objetivo Principal
Sistema y repositorio de desarrollo de software.

Este documento establece las bases arquitectónicas, directivas operativas y contexto técnico esencial para mantener la coherencia y calidad a través de múltiples sesiones de trabajo y entre diversos agentes de código o desarrolladores.

---

## 2. Reglas de Desarrollo y Buenas Prácticas
1. **Regla Crítica de Actualización (Obligatoria):**
   - Toda corrección, mejora, alteración o nueva implementación en el código debe concluir **siempre y de manera obligatoria** con la actualización de los registros dentro de `contextbase/` (`changelog.md`, `tasklist.md` y este documento si hay cambios estructurales).
2. **Minimalismo y Simplicidad:**
   - Evitar complejidad accidental, dependencias innecesarias o abstracciones prematuras.
   - Preferir soluciones limpias, mantenibles y de ejecución directa.
3. **Calidad de Código y Estilo:**
   - Mantener consistencia en el estilo, tipado y convenciones del proyecto.
   - No dejar código muerto ni archivos huérfanos.
4. **Idioma de Documentación:**
   - Todas las notas técnicas, bitácoras y registros en `contextbase/` deben mantenerse estrictamente en **español**.
5. **Mantenimiento Preventivo Automático:**
   - Revisar `contextbase/componentes.md` al iniciar un proyecto o sesión, y regenerarlo con `contextbase audit` como verificación final al cerrar cada cambio (estado de componentes y brechas de seguridad).

---

## 3. Arquitectura y Contexto Técnico General
- **Nombre:** `updall`
- **Versión:** `0.1.0`
- **Tipo de Ecosistema:** Generic
- **Tecnologías y Frameworks Clave:** Librerías estándar / Vanilla
- **Lenguajes Dominantes:** Políglota / General
- **Dependencias Principales:** Sin dependencias externas registradas.
- **Estado de Componentes y Seguridad:** `contextbase/componentes.md` (inventario, frescura de versiones y brechas; regenerar con `contextbase audit`)

### Comandos de Ejecución y Scripts Disponibles:
- No se detectaron scripts automáticos en package.json.

---

## 4. Mapa de Estructura de Directorios Clave
```
updall/
├── contextbase/               # Memoria técnica persistente y bitácora
├── contextbase/
```

<!-- CONTEXTBASE:SYNC:START -->
## Contexto Técnico Sincronizado (auto)
> Generado por `contextbase sync`. No editar dentro de este bloque: se reemplaza completo.
- **Versión:** 0.1.0
- **Ecosistema:** Generic
- **Frameworks:** Librerías estándar / Vanilla
- **Lenguajes dominantes:** Markdown (23), JSON (14), Python (4), JavaScript (1), PowerShell (1)
- **Dependencias:** Sin dependencias externas registradas.
- **Scripts:** sin scripts
- **Directorios raíz:** .agents, .kilo, .kilocode, .opencode, contextbase
<!-- CONTEXTBASE:SYNC:END -->

---
*Generado automáticamente por ContextBase CLI el 18/11/2026.*
