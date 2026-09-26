Use Cases / Application
=======================

The application layer implements the operations the system offers, such as
creating or retrieving a resource. A use case coordinates domain objects and
the capabilities it needs from ports; it does not implement transport or
infrastructure details.

Application code may depend on the domain and port contracts, but not on
FastAPI, a database driver, or a concrete adapter. This keeps the same
business operation callable from different entry points and straightforward
to test with fakes for its ports.

In kortexa, ``skills/create_skill/use_case.py`` implements ``CreateSkill``.
It creates a domain ``Skill`` and stores it through the repository port.
