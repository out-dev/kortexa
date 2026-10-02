Dependencies / Wiring
=====================

Dependency wiring is the composition root: the outermost part of the
application that creates concrete adapters and supplies them to use cases.
It connects implementation choices to application contracts without making
the application core depend on a framework or infrastructure implementation.

In kortexa, ordinary Python providers construct or retrieve adapters and
create use cases for Django views. Django does not provide a dependency
injection container; keep framework-specific request handling in the view and
pass ports to use cases through their normal constructor or call interface.

``skills/dependencies.py`` provides the in-memory repository and constructs
the skill use cases. The Django view calls that provider at the HTTP boundary.
