# Actividades del aula

Repositorio común de actividades AulaStep. Cada subcarpeta de `actividades/`
es una actividad en **fuente** (actividad.yml + pasos/ + recursos/).

En cada push a `main`, GitHub Actions valida TODAS las actividades y, solo si
todas están correctas, publica el catálogo en GitHub Pages: un índice raíz y
cada actividad en su subcarpeta (la URL usa el `id` del YAML).

## Añadir o actualizar una actividad

1. Crea/edita la actividad donde prefieras y valida en local:
   `uv run aulastep validate <carpeta>`
2. Copia su carpeta fuente a `actividades/` (sin el `dist/`).
3. Si es una actualización de una actividad ya repartida: sube su `version`
   y no cambies ningún `id` (reglas en el AGENTS.md del repo de AulaStep).
4. `git add -A && git commit && git push` — en unos minutos está publicada.

## Requisito

El workflow instala AulaStep desde el repositorio de la herramienta
(edita la URL en `.github/workflows/publicar.yml`).
