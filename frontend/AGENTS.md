# Frontend Agent Instructions (React)

Also read the repository root [AGENTS.md](../AGENTS.md) — it takes precedence
for conversation/process rules.

Detailed frontend agent context is organized under
[frontend/.ai/README.md](.ai/README.md), including architecture, workflows,
conventions, and reusable skills.

## Stack

- React + TypeScript + Vite
- Package management: [pnpm](https://pnpm.io/) — never use `npm`/`yarn`.
- UI components: [shadcn](https://ui.shadcn.com/)
- Data fetching, routing, and other app concerns: [TanStack](https://tanstack.com/) (Query, Router, ...)
- Architecture: **Feature-Based Architecture**, see
  [docs/source/architecture/feature-based-architecture.rst](../docs/source/architecture/feature-based-architecture.rst)

## Folder structure

```
frontend/
├── components.json        # shadcn config
└── src/
    ├── main.tsx
    ├── router.tsx           # TanStack Router root config
    ├── core/                # global, feature-crossing concerns
    │   ├── api/              # TanStack Query client, fetch wrapper
    │   ├── config/            # env.ts, constants
    │   ├── providers/         # QueryClientProvider, AuthProvider, ThemeProvider
    │   ├── types/              # shared domain types (e.g. User) used by multiple features
    │   └── styles/
    ├── components/ui/        # shadcn-generated base components, kept unmodified
    ├── layouts/               # Header, Sidebar, FullLayout, etc.
    └── features/
        └── <feature-name>/
            ├── components/     # feature-specific UI, composed from components/ui
            ├── hooks/           # feature hooks, including TanStack Query hooks
            ├── api/              # query/mutation definitions for this feature
            ├── types/
            ├── views/            # page/screen components
            └── routes.tsx         # TanStack Router routes for this feature
```

## Architecture rules

- Features are self-contained: never import from another feature's internal
  folders (`features/x/components/...` from `features/y` is forbidden).
  Shared types/logic move to `core/`.
- shadcn components are generated with `pnpm dlx shadcn@latest add <component>`
  and land in `components/ui/`; do not modify them for business needs — build
  wrappers/compositions in `features/*/components/` instead.
- All data access goes through TanStack Query hooks defined in
  `features/*/api/` or `core/api/` — no raw `fetch` calls inside components.
- Routes are defined per feature in `routes.tsx` and composed centrally in
  `src/router.tsx` via TanStack Router.

## Commands

```
pnpm install         # install dependencies
pnpm add <package>    # add a dependency
pnpm dev               # run dev server
pnpm build              # production build
pnpm test                # run tests
pnpm lint                 # lint
```
