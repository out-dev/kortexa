# Agent-Agnostic AI Setup

The repository should work with different coding agents, including GitHub
Copilot, Cursor, Claude Code, and Codex.

Use `AGENTS.md` for concise, mandatory instructions that are discoverable by
agents. Use `.ai/` for detailed context and reusable workflows. Do not place
provider-specific prompt syntax in shared files.

Keep instructions declarative and repository-focused:

- describe expected behavior and dependency boundaries;
- name the authoritative command for each validation step;
- link to deeper local documentation instead of duplicating it;
- avoid assumptions about a specific editor or model;
- never include secrets, credentials, or machine-specific paths.

A tool-specific integration may reference this shared context, but it must not
become the source of truth for repository architecture.
