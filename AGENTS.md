# kortexa — Agent Instructions

## Project overview

kortexa is a monorepo with a Python backend and a React frontend, built with an
agent-agnostic AI setup.. These instructions apply to any AI coding assistant
(GitHub Copilot, Cursor, Claude Code, Codex, ...) working in this repository.

## Repository structure

```
kortexa/
├── .ai/        # AI Workflows and skills
├── backend/    # Python, vertical Slice Architecture for code organization and Hexagonal Architecture for dependency boundaries — see docs/source/backend
├── frontend/   # React, feature-based architecture — see docs/source/frontend
├── docs/       # Sphinx documentation
```

# Conversation start rule (MANDATORY)

Whenever a **new conversation** begins, do **not** start coding immediately.

1. Investigate the documentation and codebase first. Read the relevant files and inspect existing patterns before proposing changes.
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
- Always keep documentation up to date.
- Omit subresponses and only output final response.
- At the end of every response, always include a minimalistic table listing all context sources and information that were used to generate the answer.

<instruction_priority>
- User instructions override default style, initiative, and formatting preferences.
- Always inspect ai skills in folder [sills](.ai/skills/)
- Always use skill [ponytail](.ai/skills/ponytail/SKILL.md)
- Safety, honesty, repository constraints, and permission constraints do not yield.
- If a newer instruction conflicts with an older one, follow the newer instruction and preserve all non-conflicting earlier instructions.
</instruction_priority>

## Global conventions

- Never commit secrets or real credentials; keep `.env.example` files up to date.
- Extended background and rationale (ADRs, diagrams) belongs in `docs/`, not in this file — keep this file short and actionable.
