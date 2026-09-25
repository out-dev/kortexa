# kortexa — Agent Instructions

## Project overview

kortexa is a monorepo with a Python backend and a React frontend, built with an
agent-agnostic AI setup [.ai\architecture\agent-agnostic-ai.md](.ai\architecture\agent-agnostic-ai.md). These instructions apply to any AI coding assistant
(GitHub Copilot, Cursor, Claude Code, Codex, ...) working in this repository.

## Repository structure

```
kortexa/
├── backend/    # Python, hexagonal architecture — see backend/AGENTS.md
├── frontend/   # React, feature-based architecture — see frontend/AGENTS.md
└── docs/       # Sphinx documentation
```

- Backend-specific rules: [backend/AGENTS.md](backend/AGENTS.md)
- Frontend-specific rules: [frontend/AGENTS.md](frontend/AGENTS.md)
- Shared agent context: [.ai/README.md](.ai/README.md)
- Each subproject manages its own dependencies independently (no shared
  monorepo build tool). Never run a package manager command from the wrong
  subfolder.

# Conversation start rule (MANDATORY)

Whenever a **new conversation** begins, do **not** start coding immediately.

1. Investigate the codebase first. Read the relevant files and inspect existing patterns before proposing changes.
2. Identify what is unclear, risky, or ambiguous about the requested change.
3. Ask the user **3-10 clarifying questions in a numbered list** (not bullets).
4. Only after those questions are answered, start implementing. For follow-up turns in the same conversation, do not repeat this step unless a new ambiguity appears.

# Prompting and execution principles

- Prefer short, explicit, high-signal instructions over long repetitive ones.
- Preserve the user's task intent and make the smallest change that fully solves the request.
- Separate rules, context, and deliverables clearly. Use Markdown sections and XML-style blocks when they improve instruction following.
- Ground decisions in repository evidence. Inspect files before assuming patterns, architecture, or naming.
- After the mandatory start-of-conversation questions are answered, continue proactively on reversible, low-risk steps instead of asking for unnecessary confirmation.
- If context can be retrieved from the repo, retrieve it before asking the user.
- When a task is blocked by a real ambiguity, ask only the minimum follow-up needed to unblock the work.
- Always keep documentation and ai setup up to date.
- At the end of every response, always include a table listing all context sources and information that were used to generate the answer.

<instruction_priority>
- User instructions override default style, initiative, and formatting preferences.
- Safety, honesty, repository constraints, and permission constraints do not yield.
- If a newer instruction conflicts with an older one, follow the newer instruction and preserve all non-conflicting earlier instructions.
</instruction_priority>

## Documentation

Detailed architecture and API documentation lives in `docs/`, built with
[Sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html). The
`docs/` folder is its own `uv`-managed Python project (own `pyproject.toml`
and lockfile, independent of `backend/`):

```
cd docs
uv sync                       # install Sphinx + extensions
uv run sphinx-build -b html source build   # or: make html
```

Backend and frontend documentation lives in `docs/source/backend/` and
`docs/source/frontend/`. Cross-cutting content (architecture overview, ADRs)
lives directly in `docs/source/`. The backend and frontend implementations
have been removed; their retained project guides describe the former baseline.
Update the `.rst` files under `docs/source/` whenever an architectural
decision changes.

## Global conventions

- Never commit secrets or real credentials; keep `.env.example` files up to date.
- Keep commit messages and PRs focused on a single logical change.
- Extended background and rationale (ADRs, diagrams) belongs in `.ai/README.md`
  or `docs/`, not in this file — keep this file short and actionable.
