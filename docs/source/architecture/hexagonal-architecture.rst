Hexagonal Architecture
=======================

Hexagonal Architecture, also called Ports and Adapters, organizes an
application around its business capabilities rather than around technical
infrastructure. The central idea is that business rules should remain usable
and testable when the database, web framework, external APIs, or user
interface changes.

The name describes a conceptual shape, not a required number of packages or
interfaces. Each side of the hexagon represents a possible interaction with
the application. The important property is the boundary between the
application core and the outside world.

Core Principle
--------------

The application core owns the rules that give the system its meaning. It must
not depend on a particular database driver, HTTP framework, cloud SDK, queue,
or model provider. External technology depends on contracts defined by the
core instead.

This dependency direction makes infrastructure replaceable. A use case can be
executed from an HTTP endpoint, a command-line entry point, a scheduled job,
or a message consumer without changing the business rules themselves.

The Three Main Parts
--------------------

Domain and application core
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The core contains the behavior of the system and is split conceptually into
 two responsibilities:

* The **domain** models business concepts and invariants. It contains entities,
  value objects, aggregates, domain services, domain events, and domain
  exceptions where those concepts are useful.
* The **application layer** coordinates use cases. It defines the application
  workflows, controls transaction boundaries where appropriate, and invokes
  ports. It should not contain persistence queries or HTTP details.

A domain entity has an identity and a lifecycle. A value object is defined by
its values and is commonly immutable. An aggregate groups related objects
behind an aggregate root, which protects consistency when state changes. A
domain service is appropriate for business behavior that does not naturally
belong to one entity or value object.

Ports
~~~~~

Ports are contracts at the boundary of the core. They describe what the core
needs or exposes without prescribing how the operation is implemented. Python
``Protocol`` classes or abstract base classes are suitable representations.

Two useful categories are:

* **Inbound ports** describe use cases that the outside world may invoke.
  They provide an application-facing interface for adapters such as an HTTP
  controller, command handler, or message consumer.
* **Outbound ports** describe capabilities required by the core, such as
  loading an aggregate, publishing an event, sending a notification, reading
  a clock, or calling an AI provider.

A repository port, for example, can express operations such as retrieving,
creating, and updating an aggregate. It does not expose SQL statements,
ORM models, sessions, or a vendor-specific query language.

Adapters
~~~~~~~~

Adapters translate between an external technology and a port. An inbound API
adapter maps HTTP requests into use-case inputs and maps use-case results into
HTTP responses. An outbound persistence adapter maps domain objects to database
records and back again. Other outbound adapters can implement messaging,
email, file storage, third-party APIs, or model providers.

Multiple adapters may implement one port. This is useful for a production
adapter, an in-memory adapter for unit tests, and a local development adapter.
The core should not need to know which implementation is active.

Dependency Direction
--------------------

Dependencies point inward:

.. code-block:: text

   inbound adapters -> application ports -> domain
   outbound adapters -> outbound ports -> application/domain
   infrastructure ---------------> wiring and configuration

The domain should be the most stable part of the system. The application layer
may depend on domain concepts and port contracts. Adapters may depend on the
core contracts, but the domain and application layers must not import adapter
implementations.

Framework code belongs at the edge. FastAPI routers, Pydantic transport
schemas, SQLAlchemy models, cloud SDKs, and provider-specific request formats
should be translated at adapter boundaries rather than passed through the
core.

Domain-Driven Design Relationship
---------------------------------

Hexagonal Architecture defines how dependencies cross the system boundary.
Domain-Driven Design defines how the business problem is understood and
modeled within the core. They complement each other but are not the same
thing.

DDD starts with the domain and its language. Developers and domain experts
establish a **ubiquitous language** so that important concepts have consistent
names in conversations, documentation, code, and tests. The domain is then
organized around meaningful boundaries, which may become bounded contexts.

A DDD-oriented domain commonly includes:

* entities with identity and lifecycle;
* value objects that express validated concepts;
* aggregates that protect invariants and define consistency boundaries;
* repositories that abstract aggregate persistence;
* domain services for behavior that belongs to the domain but not one object;
* domain events for facts that have happened inside the domain.

DDD should be applied proportionally. Simple CRUD behavior does not require a
large domain model. The architecture should make complex business rules
clearer, not add ceremony where no business complexity exists.

Typical Request Flow
--------------------

A request through an HTTP API typically follows this path:

#. An inbound adapter validates transport-level input and translates it into
   an application command or query.
#. An application use case loads required aggregates through outbound ports.
#. Domain objects enforce invariants and perform business behavior.
#. The use case persists changes or publishes domain events through ports.
#. The inbound adapter translates the result or a known error into a transport
   response.

At no point does the domain need to know that the request arrived through
HTTP or that state was stored in a particular database.

Testing Strategy
----------------

The boundaries produce a natural testing strategy:

* Domain tests exercise business invariants without frameworks or I/O.
* Application tests use fakes or mocks for outbound ports and verify workflows.
* Adapter tests verify translation and integration with the selected
  infrastructure.
* End-to-end tests verify that the assembled system behaves correctly through
  a real entry point.

The most valuable tests for business behavior should therefore be fast and
independent of network services, databases, and provider credentials.

Applying the Pattern
--------------------

When adding a capability, identify the business concept and use case first.
Model the domain behavior, define the ports needed by the application service,
implement adapters for the selected technologies, and assemble them through
configuration and dependency injection. Keep transport schemas and
persistence models separate from domain objects when their concerns differ.

A useful implementation shape is::

   src/<package>/
       domain/<bounded_context>/
       application/<bounded_context>/
       ports/inbound/
       ports/outbound/
       adapters/inbound/
       adapters/outbound/
       infrastructure/

This is a guide rather than a rule that every project must copy literally.
The architectural test is whether the core remains independent, the ports
express meaningful boundaries, and adapters can be replaced without rewriting
business behavior.

Relation to kortexa
-------------------

The Python backend uses this architecture to keep business behavior separate
from FastAPI, persistence, external services, and AI providers. AI providers
are outbound adapters behind a provider port, allowing the selected provider
to change without coupling the domain or application layer to one vendor.

Further Reading
---------------

This description is based on *Building Maintainable Python Applications with
Hexagonal Architecture and Domain-Driven Design* by Hieu Tran. The article
introduces the Ports and Adapters pattern, explains its relationship with DDD,
and demonstrates a Python structure containing application services, domains,
ports, adapters, routers, and infrastructure.
