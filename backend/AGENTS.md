# Backend Agent Instructions (Python)

Also read the repository root [AGENTS.md](../AGENTS.md) — it takes precedence
for conversation/process rules.

Detailed backend agent context is organized under
[backend/.ai/README.md](.ai/README.md), including architecture, workflows,
conventions, and reusable skills.

## Stack

- Python, [FastAPI](https://fastapi.tiangolo.com/)
- Package management: [uv](https://docs.astral.sh/uv/) — never use `pip install` directly.
- Architecture: **Hexagonal Architecture (Ports & Adapters)**, see
  [docs/source/architecture/hexagonal-architecture.rst](../docs/source/architecture/hexagonal-architecture.rst)

## Folder structure

```
backend/
├── src/kortexa_backend/
│   ├── main.py             # entry point, DI wiring
│   ├── domain/              # entities, value objects, domain events, exceptions — no external deps
│   │   └── <bounded_context>/
│   ├── application/         # use cases / application services, orchestrate domain + ports
│   │   └── <bounded_context>/
│   ├── ports/                # abstract interfaces (Protocols/ABCs)
│   │   ├── inbound/
│   │   └── outbound/         # e.g. repository, AI-provider interfaces
│   ├── adapters/              # concrete implementations of ports
│   │   ├── inbound/api/       # FastAPI routers, request/response schemas
│   │   └── outbound/
│   │       ├── persistence/
│   │       └── ai_providers/  # concrete AI/LLM provider adapters
│   └── infrastructure/        # logging, config, DI container, middleware
└── tests/
    ├── unit/                  # domain + application, no adapters
    └── integration/           # adapters against real/faked infrastructure
```

## Architecture rules

- Dependency direction: `domain` depends on nothing in this repo; `application`
  depends only on `domain` and `ports`; `adapters` implement `ports` and may
  depend on `application`/`domain` — never the reverse.
- New functionality = new or extended bounded context under `domain/` and
  `application/`, plus ports/adapters as needed. Do not put business logic
  directly in `main.py` or in adapters.
- AI/LLM providers are accessed only through an outbound port
  (`ports/outbound/ai_provider.py`); concrete providers (OpenAI, Azure,
  Anthropic, local models, ...) are adapters under
  `adapters/outbound/ai_providers/`, selected via configuration/DI so the
  provider can be swapped without touching `domain`/`application`.

## Commands

```
uv sync                                              # install dependencies
uv add <package>                                     # add a dependency
uv run uvicorn kortexa_backend.main:app --reload     # run dev server
uv run pytest                                        # run tests
uv run ruff check .                                  # lint
```

## Testing

- Unit tests cover `domain`/`application` without real infrastructure (ports
  are faked/mocked).
- Integration tests exercise adapters against real or containerized
  infrastructure.
- Run `uv run pytest` after any change and fix failures before finishing.
