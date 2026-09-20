Backend
=======

The Python backend is built with FastAPI and follows Hexagonal Architecture.

Development
-----------

Run these commands from the ``backend/`` directory::

   uv sync
   uv run uvicorn kortexa_backend.main:app --reload
   uv run pytest
   uv run ruff check .

The application reads typed settings from environment variables with the
``KORTEXA_`` prefix. The available baseline settings are:

``KORTEXA_APP_NAME``
   Application title. Defaults to ``kortexa backend API``.
``KORTEXA_ENVIRONMENT``
   Runtime environment name. Defaults to ``development``.
``KORTEXA_CORS_ORIGINS``
   JSON list of browser origins allowed to call the API. Defaults to
   ``["http://localhost:5173"]``.

Health endpoints
----------------

``GET /api/v1/health/live`` and ``GET /api/v1/health/ready`` return HTTP 200 with::

   {"status": "ok"}

Readiness is process-based in the baseline. External dependency checks will be
added when outbound adapters are introduced.

Package boundaries
------------------

``domain`` contains framework-independent business rules. ``application``
contains use cases. ``ports`` defines inbound and outbound interfaces.
``adapters`` connects those interfaces to HTTP and external services.
``infrastructure`` contains configuration and application wiring.

The API reference is auto-generated from the backend source tree by
``sphinx-autoapi``.
