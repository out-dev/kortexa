"""Sphinx configuration for kortexa documentation."""

import shutil
from pathlib import Path

project = "kortexa"
copyright = "2026, kortexa"
author = "kortexa"
release = "0.1.0"

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

html_theme = "furo"
html_static_path = ["_static"]

# Backend and frontend own their narrative docs (backend/docs, frontend/docs)
# so they live next to the code; sync them into source/ before each build.
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_DOC_SOURCES = {
    _REPO_ROOT / "backend" / "docs": Path(__file__).resolve().parent / "backend",
    _REPO_ROOT / "frontend" / "docs": Path(__file__).resolve().parent / "frontend",
}


def _sync_project_docs(app):
    for src, dest in _DOC_SOURCES.items():
        if src.is_dir():
            shutil.copytree(src, dest, dirs_exist_ok=True)


def setup(app):
    app.connect("builder-inited", _sync_project_docs)
