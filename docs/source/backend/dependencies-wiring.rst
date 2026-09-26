Dependencies / Wiring
=====================

Dependency wiring is the composition root: the outermost part of the
application that creates concrete adapters and supplies them to use cases.
It connects implementation choices to application contracts without making
the application core depend on a framework or infrastructure implementation.

In a FastAPI application, dependency providers can construct or retrieve an
adapter and inject it into an endpoint using ``Depends``. FastAPI-specific
wiring stays at the edge; use cases continue to accept ports through their
normal constructor or call interface.

In kortexa, ``skills/dependencies.py`` provides the repository and constructs
the skill use cases. The endpoint receives those use cases through FastAPI
dependencies.
