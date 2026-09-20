# Repository Architecture

kortexa is a monorepo with independently managed `backend/`, `frontend/`, and
`docs/` projects.

- `backend/` contains the Python application and follows Hexagonal Architecture.
- `frontend/` contains the React application and follows Feature-Based Architecture.
- `docs/` contains the uv-managed Sphinx project and cross-cutting documentation.
- `backend/docs/` and `frontend/docs/` contain documentation next to their code.

The backend and frontend have independent dependency management. Run `uv`
commands from `backend/` or `docs/`, and `pnpm` commands from `frontend/`.
Do not introduce root-level package management unless the repository decision
changes explicitly.

The detailed generic architecture references are:

- `docs/source/architecture/hexagonal-architecture.rst`
- `docs/source/architecture/feature-based-architecture.rst`
