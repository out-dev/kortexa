Ports
=====

Ports are interfaces at the boundary between the application core and the
outside world. They state what the application needs or what operation it
offers, without prescribing which technology provides it.

An outbound port might describe repository operations or access to an
external service. An inbound port can describe an application operation
that an entry point invokes. Python ``Protocol`` classes and abstract base
classes are both suitable ways to define these contracts.

In kortexa, ``skills/ports/skill_repository.py`` defines the ``SkillRepository``
protocol. It describes adding and retrieving skills without exposing a
database, ORM, or storage-specific API.
