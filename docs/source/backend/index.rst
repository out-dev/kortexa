Backend
=======

The backend implementation has been removed. The baseline details below are
retained as historical reference documentation.

Architecture
------------

The Python backend was built with FastAPI and follows Hexagonal Architecture.
``domain`` contains framework-independent business rules. ``application``
contains use cases. ``ports`` defines inbound and outbound interfaces.
``adapters`` connects those interfaces to HTTP and external services.
``infrastructure`` contains configuration and application wiring.

Development
-----------

These commands describe the removed baseline and are no longer runnable::

   uv sync
   uv run uvicorn kortexa_backend.main:app --reload
   uv run pytest
   uv run ruff check .

The baseline application read typed settings from environment variables with
the ``KORTEXA_`` prefix: app name, environment, and CORS origins.

Health endpoints
----------------

The baseline exposed ``GET /api/v1/health/live`` and
``GET /api/v1/health/ready``, both returning ``{"status": "ok"}``.

The API reference is no longer generated because the backend source tree has
been removed.
