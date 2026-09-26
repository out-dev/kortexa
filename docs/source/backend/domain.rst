Domain
======

The domain is the business core of the backend. It represents the concepts,
rules, and invariants that give the product its meaning. Domain code should
not depend on FastAPI, databases, or other infrastructure, so business rules
remain usable and testable when those technologies change.

Domain models commonly include entities with identity, value objects defined
by their values, and domain services for rules that do not belong to one
object. They validate business invariants rather than HTTP or persistence
concerns.

In kortexa, ``skills/domain/skill.py`` defines the ``Skill`` model and enforces
that its identifier and content are valid when a skill is created.
