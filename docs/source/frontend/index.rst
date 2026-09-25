Frontend
========

The frontend implementation has been removed. The baseline details below are
retained as historical reference documentation.

The React application was built with Vite following Feature-Based Architecture.
It used TanStack Router and TanStack Query, with feature modules under
``src/features``. The health feature called the versioned backend API through
``VITE_API_BASE_URL``. A theme provider persisted the light/dark choice in
local storage.

Development
-----------

These commands describe the removed baseline and are no longer runnable::

   pnpm install
   pnpm dev
   pnpm lint
   pnpm build
   pnpm test

Backend API
-----------

The former frontend API client used ``VITE_API_BASE_URL`` as its base URL. Its
local baseline value was::

   VITE_API_BASE_URL=http://localhost:8000/api/v1

The baseline health endpoints were ``/health/live`` and ``/health/ready``
relative to that versioned base URL.
