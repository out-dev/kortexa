# Documentation Architecture

Documentation has three responsibilities:

- `AGENTS.md` contains short operational instructions for coding agents.
- `.ai/` contains detailed agent-oriented context, workflows, and skills.
- Sphinx documentation contains human-facing architecture and API reference.

Cross-cutting Sphinx content lives under `docs/source/`. Backend narrative
documentation lives under `backend/docs/`, and frontend narrative
documentation lives under `frontend/docs/`. The Sphinx configuration copies
those project-local folders into the generated source tree during a build.

Edit the source documentation next to the relevant project. Do not edit the
generated `docs/source/backend/` or `docs/source/frontend/` folders.

Build documentation from `docs/` with:

```text
uv sync
uv run sphinx-build -b html source build
```
