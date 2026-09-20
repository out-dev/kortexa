# React and TypeScript Conventions

Use pnpm for dependency management. Keep feature code co-located and use
explicit TypeScript types at API and shared-domain boundaries.

Use TanStack Query for server state and TanStack Router for route composition.
Components should consume feature hooks instead of making raw requests.

Use shadcn for generic UI primitives. Put business-specific composition and
labels in feature components rather than modifying shared primitives for one
feature.
