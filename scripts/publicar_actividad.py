#!/usr/bin/env python3
"""Publica actividades AulaStep desde el equipo local."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ACTIVITIES = ROOT / "actividades"
PAGES_BRANCH = "gh-pages"
CATALOG_TITLE = "Actividades · Santiago Galván"
SETUP_PATHS = (
    Path(".gitignore"),
    Path("README.md"),
    Path("scripts/publicar_actividad.py"),
    Path(".github/workflows/publicar.yml"),
)


def use_project_venv() -> None:
    """Use the repository environment when the script is run directly."""
    venv_python = ROOT / ".venv" / "bin" / "python"
    if venv_python.is_file() and Path(sys.prefix).resolve() != (ROOT / ".venv").resolve():
        os.execv(str(venv_python), [str(venv_python), *sys.argv])


use_project_venv()

from jinja2 import Environment, PackageLoader, select_autoescape  # noqa: E402
from aulastep import branding  # noqa: E402
from aulastep.project import load_project  # noqa: E402
from aulastep.publish import _badge, _git_dates, _normalize  # noqa: E402


class PublishError(Exception):
    pass


def run(*args: str, cwd: Path = ROOT, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, text=True, capture_output=capture, check=True)


def aulastep_command() -> str:
    return os.environ.get("AULASTEP", str(Path(sys.executable).with_name("aulastep")))


def require_main_branch() -> None:
    branch = run("git", "branch", "--show-current", capture=True).stdout.strip()
    if branch != "main":
        raise PublishError("Ejecuta el script desde la rama main.")
    staged = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT).returncode
    if staged != 0:
        raise PublishError("Hay cambios preparados para commit. Confírmalos o retíralos antes de publicar.")


def project(path: Path):
    zone_identifiers = sorted(path.rglob("*:Zone.Identifier"))
    if zone_identifiers:
        names = "\n".join(f"  - {file.relative_to(path)}" for file in zone_identifiers)
        raise PublishError(
            f"La actividad contiene archivos ':Zone.Identifier' creados por Windows. Elimínalos antes de publicar:\n{names}"
        )
    loader = load_project(path)
    if not loader.report.ok or loader.compiled is None or loader.config is None:
        raise PublishError(f"La actividad '{path}' no es válida. Corrige sus errores antes de publicar.")
    return loader


def cleanup_zone_identifiers(path: Path) -> None:
    files = sorted(path.rglob("*:Zone.Identifier"))
    for file in files:
        file.unlink()
    if files:
        print(f"Eliminados {len(files)} archivos ':Zone.Identifier' de '{path}'.")


def activity_dirs() -> list[Path]:
    directories = []
    for path in ACTIVITIES.iterdir():
        manifest = path / "actividad.yml"
        # Draft folders outside Git belong to local work and must not block a publication.
        tracked = subprocess.run(
            ["git", "ls-files", "--error-unmatch", "--", str(manifest.relative_to(ROOT))],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ).returncode == 0
        if manifest.is_file() and tracked:
            directories.append(path)
    return sorted(directories, key=lambda p: p.name)


def catalog_entries() -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    ids: dict[str, Path] = {}
    for activity_dir in activity_dirs():
        loader = project(activity_dir)
        if not loader.config.actividad.publicada:
            continue
        meta = loader.compiled.activity
        activity_id = str(meta["id"])
        if activity_id in ids:
            raise PublishError(
                f"El ID '{activity_id}' está repetido en '{activity_dir.name}' y '{ids[activity_id].name}'."
            )
        ids[activity_id] = activity_dir
        created, updated = _git_dates(activity_dir)
        entries.append(
            {
                "id": activity_id,
                "titulo": meta["titulo"],
                "subtitulo": meta.get("subtitulo", ""),
                "descripcion": meta.get("descripcion", ""),
                "modulo": meta.get("modulo", ""),
                "curso": meta.get("curso", ""),
                "duracion": meta.get("duracionMinutos"),
                "version": meta.get("version", ""),
                "autor": meta.get("autor", ""),
                "licencia": meta.get("licencia", {}),
                "pasos": len(loader.compiled.steps),
                "actualizada": updated,
                "badge": _badge(created, updated),
                "buscar": _normalize(
                    " ".join(
                        str(meta.get(key, "") or "")
                        for key in ("titulo", "subtitulo", "descripcion", "modulo", "curso", "autor")
                    )
                ),
            }
        )
    return entries


def write_catalog(output: Path) -> None:
    entries = catalog_entries()
    if not entries:
        raise PublishError("No hay actividades publicadas para incluir en el catálogo.")
    environment = Environment(
        loader=PackageLoader("aulastep", "templates"),
        autoescape=select_autoescape(["html", "j2"]),
    )
    html = environment.get_template("publish-index.html.j2").render(
        title=CATALOG_TITLE,
        entries=entries,
        modulos=sorted({entry["modulo"] for entry in entries if entry["modulo"]}),
        app_name=branding.APP_NAME,
        app_version=branding.APP_VERSION,
    )
    (output / "index.html").write_text(html, encoding="utf-8")


def remote_has_pages_branch() -> bool:
    result = subprocess.run(
        ["git", "ls-remote", "--exit-code", "--heads", "origin", PAGES_BRANCH],
        cwd=ROOT,
        text=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


@contextmanager
def pages_worktree(allow_new: bool):
    exists = remote_has_pages_branch()
    if not exists and not allow_new:
        raise PublishError(
            "La rama gh-pages todavía no existe. Ejecuta primero 'reconstruir' para crear la publicación inicial."
        )

    temporary = tempfile.TemporaryDirectory(prefix="actividades-pages-")
    path = Path(temporary.name)
    if exists:
        run("git", "fetch", "origin", PAGES_BRANCH)
        run("git", "worktree", "add", "--detach", str(path), f"origin/{PAGES_BRANCH}")
    else:
        run("git", "worktree", "add", "--detach", str(path), "HEAD")
        run("git", "switch", "--orphan", PAGES_BRANCH, cwd=path)
        run("git", "rm", "-rf", ".", cwd=path)

    try:
        yield path
    finally:
        subprocess.run(["git", "worktree", "remove", "--force", str(path)], cwd=ROOT, check=False)
        temporary.cleanup()


def copy_source(source: Path, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    run(
        "rsync",
        "-a",
        "--delete",
        "--exclude=.git/",
        "--exclude=dist/",
        f"{source}/",
        f"{target}/",
    )


def version_tuple(version: str) -> tuple[int, int, int]:
    return tuple(int(part) for part in version.split("."))  # type: ignore[return-value]


def commit_paths(paths: tuple[Path, ...], message: str) -> bool:
    relative_paths = tuple(str(path) for path in paths)
    status = subprocess.run(
        ["git", "status", "--porcelain", "--", *relative_paths], cwd=ROOT, text=True, capture_output=True
    ).stdout
    if not status:
        return False
    run("git", "add", "-A", "--", *relative_paths)
    run("git", "commit", "--only", "-m", message, "--", *relative_paths)
    run("git", "push", "origin", "main")
    return True


def commit_publisher_setup() -> None:
    commit_paths(SETUP_PATHS, "configura publicación local")


def commit_source(target: Path, activity_id: str, version: str) -> None:
    if not commit_paths((target.relative_to(ROOT),), f"actualiza actividad {activity_id} a {version}"):
        raise PublishError("La fuente no cambió; no hay nada que publicar. Usa 'reconstruir' si cambió AulaStep.")


def commit_pages(pages: Path, activity_id: str, version: str) -> None:
    run("git", "add", "-A", cwd=pages)
    if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=pages).returncode == 0:
        print("El sitio publicado ya estaba actualizado.")
        return
    run("git", "commit", "-m", f"publica {activity_id} {version}", cwd=pages)
    run("git", "push", "origin", f"HEAD:{PAGES_BRANCH}", cwd=pages)


def publish(source_arg: str) -> None:
    require_main_branch()
    commit_publisher_setup()
    source = Path(source_arg).expanduser().resolve()
    if not (source / "actividad.yml").is_file():
        raise PublishError("La ruta debe ser una carpeta de actividad que contenga actividad.yml.")
    cleanup_zone_identifiers(source)

    incoming = project(source)
    incoming_id = incoming.config.actividad.id
    matches = [directory for directory in activity_dirs() if project(directory).config.actividad.id == incoming_id]
    if len(matches) > 1:
        raise PublishError(f"Ya hay más de una actividad local con el ID '{incoming_id}'.")
    target = matches[0] if matches else ACTIVITIES / source.name
    previous = project(target) if (target / "actividad.yml").is_file() else None
    if previous and previous.config.actividad.id != incoming_id:
        raise PublishError("No cambies el ID de una actividad existente: define su URL pública.")
    if previous and source != target and version_tuple(incoming.config.actividad.version) <= version_tuple(previous.config.actividad.version):
        raise PublishError("Una actualización debe tener una versión mayor que la publicada en el repositorio.")

    run(aulastep_command(), "validate", str(source))
    if source != target:
        copy_source(source, target)
    copied = project(target)
    commit_source(target, copied.config.actividad.id, copied.config.actividad.version)

    if not remote_has_pages_branch():
        rebuild()
        return

    with pages_worktree(False) as pages:
        destination = pages / copied.config.actividad.id
        if copied.config.actividad.publicada:
            run(aulastep_command(), "build", str(target), "--output", str(destination), "--clean")
        else:
            shutil.rmtree(destination, ignore_errors=True)
        write_catalog(pages)
        commit_pages(pages, copied.config.actividad.id, copied.config.actividad.version)


def rebuild() -> None:
    require_main_branch()
    commit_publisher_setup()
    cleanup_zone_identifiers(ACTIVITIES)
    catalog_entries()  # Validates all sources and duplicate IDs before rebuilding the site.
    with pages_worktree(True) as pages:
        run("git", "rm", "-rf", ".", cwd=pages)
        run(aulastep_command(), "publish", str(ACTIVITIES), "--output", str(pages), "--title", CATALOG_TITLE)
        commit_pages(pages, "catálogo completo", "")


def main() -> None:
    parser = argparse.ArgumentParser(description="Publica actividades AulaStep desde este repositorio.")
    commands = parser.add_subparsers(dest="command", required=True)
    publish_parser = commands.add_parser("publicar", help="Confirma y publica una actividad.")
    publish_parser.add_argument("carpeta", help="Carpeta que contiene actividad.yml.")
    commands.add_parser("reconstruir", help="Reconstruye todo el sitio y crea gh-pages si no existe.")
    args = parser.parse_args()

    try:
        if args.command == "publicar":
            publish(args.carpeta)
        else:
            rebuild()
    except (PublishError, subprocess.CalledProcessError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
