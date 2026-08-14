# Actividades del aula

Repositorio común de actividades AulaStep. Cada subcarpeta de `actividades/`
es una actividad en **fuente** (actividad.yml + pasos/ + recursos/).

La publicación se hace desde el equipo local con `scripts/publicar_actividad.py`.
La rama `main` guarda las fuentes y `gh-pages` el sitio estático publicado.
GitHub Pages debe configurarse para desplegar desde la rama `gh-pages`, carpeta
`/ (root)`.

## Añadir o actualizar una actividad

1. Crea o edita la actividad fuera de este repositorio.
2. Para una actualización, incrementa `actividad.version` y conserva
   `actividad.id`: el ID define la URL pública.
3. Publica la actividad:
   ```bash
   ./scripts/publicar_actividad.py publicar "/ruta/a/la/actividad"
   ```

El script valida la actividad, la copia en `actividades/` sin `dist/`, compila
solo esa actividad, actualiza el catálogo y sube los cambios de `main` y
`gh-pages`. También elimina automáticamente los archivos `:Zone.Identifier`
que Windows puede añadir al copiar archivos.

## Primera publicación y reconstrucción completa

Para la primera actividad, ejecuta el comando `publicar` con su carpeta. El
script confirma la fuente en `main`, crea `gh-pages` y hace una compilación
completa inicial automáticamente:

```bash
./scripts/publicar_actividad.py publicar "actividades/Nombre de la actividad"
```

Tras actualizar AulaStep, ejecuta:

```bash
./scripts/publicar_actividad.py reconstruir
```

Este comando valida y recompila todas las actividades, crea `gh-pages` si no
existe y la publica. Las publicaciones habituales no recompilan las actividades
sin cambios.

## Eliminar una actividad

Usá el valor de `actividad.id`, no el nombre de la carpeta:

```bash
./scripts/publicar_actividad.py eliminar configuracion-red-interna-linux
```

El script elimina la fuente de `main`, su sitio en `gh-pages`, actualiza el
catálogo y sube ambos cambios. No permite borrar la última actividad publicada.

## Requisito

El script usa automáticamente `.venv/bin/python` y su instalación de AulaStep.
Si usás otra instalación, definí la variable `AULASTEP` con la ruta al ejecutable.
