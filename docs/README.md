# Documentation

This folder contains kortexa's Sphinx documentation project, managed
independently with `uv`.

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
- `source/backend/` contains the backend guide.
- `source/index.rst` defines the documentation table of contents.
- `source/conf.py` configures Sphinx.

Update documentation in `source/` directly.
