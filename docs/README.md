# Documentation

This folder contains kortexa's Sphinx documentation project. It is managed
independently from the backend and frontend projects with `uv`.

## Build

From this directory, install the documentation dependencies and build the HTML
site:

```powershell
uv sync
uv run sphinx-build -b html source build
```

The generated site is in `build/`. To preview changes automatically while
editing, run:

```powershell
uv run sphinx-autobuild source build
```

## Structure

- `source/architecture/` contains shared architecture documentation.
- `source/backend/` and `source/frontend/` contain the retained project guides.
- `source/index.rst` defines the documentation table of contents.
- `source/conf.py` configures Sphinx.

Backend and frontend guides describe the former baseline; their implementations
have been removed. Update documentation in `source/` directly.
