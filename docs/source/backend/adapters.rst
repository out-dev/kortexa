Adapters
========

Adapters connect ports to concrete technologies. They translate between the
port's application-facing contract and an external system's API or data
format. An adapter may use an in-memory collection, a database, a cache, or
an external service.

An adapter implements a port; the application depends on the port rather
than selecting or constructing an adapter itself. This makes it possible to
replace an implementation without changing business behavior.

In kortexa, ``skills/adapters/in_memory_skill_repository.py`` implements the
skill repository using an in-memory dictionary. A persistent repository
could implement the same port later.
