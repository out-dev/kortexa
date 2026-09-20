Frontend
========

React frontend, built with Vite following Feature-Based Architecture.

Install and run the application from the ``frontend/`` directory::

   pnpm install
   pnpm dev
   pnpm lint
   pnpm build
   pnpm test

The application uses TanStack Router and TanStack Query with feature modules
under ``src/features``. The health feature calls the versioned backend API
through ``VITE_API_BASE_URL``. A theme provider persists the light/dark choice
in local storage.

Backend API
-----------

The frontend API client should use ``VITE_API_BASE_URL`` as its base URL. For
local development, configure it as::

   VITE_API_BASE_URL=http://localhost:8000/api/v1

The baseline health endpoints are ``/health/live`` and ``/health/ready``
relative to that versioned base URL.
