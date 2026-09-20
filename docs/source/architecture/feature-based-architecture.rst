Feature-Based Architecture
===========================

Feature-Based Architecture organizes a frontend by the capabilities users
interact with rather than by technical file type. Components, hooks, API
operations, types, views, routes, and tests for one capability live together.
This keeps a feature's behavior discoverable and limits the amount of the
application that must be understood when the feature changes.

The Problem with Type-Based Organization
----------------------------------------

A type-based structure places all components in one folder, all hooks in
another, all pages in another, and all types somewhere else. This can be
comfortable for a small application, but related code becomes scattered as
the application grows. A change to one capability requires navigating many
global folders and makes ownership boundaries difficult to see.

Feature-based organization makes the capability the primary unit of change.
A feature can be developed, tested, reviewed, and removed as a coherent part
of the product.

Main Building Blocks
--------------------

Core
~~~~

``core`` contains application-wide concerns that are not owned by one feature.
Examples include environment configuration, the API client, global styles,
theme setup, providers, shared infrastructure, and domain models used by
multiple features.

Core is not a dumping ground for convenient code. A module belongs in core
when it represents a genuinely shared contract or cross-cutting capability.
Code that is used by only one feature should remain inside that feature.

Layouts
~~~~~~~

Layouts define application-level composition such as headers, sidebars,
navigation shells, authenticated frames, and full-page wrappers. They arrange
features without owning their business rules. A layout can be shared by many
routes while each feature remains responsible for its own content and behavior.

Features
~~~~~~~~

Each feature represents a user-facing capability or a meaningful domain area.
A feature is intentionally cohesive and can contain the files it needs:

.. code-block:: text

   src/features/<feature>/
       components/    feature-specific UI
       hooks/         feature-specific React hooks
       api/           queries, mutations, and API mappings
       types/         types used only by the feature
       views/         screens or route-level compositions
       routes.tsx     feature-owned route definitions
       *.test.tsx     feature tests, when co-located

The exact subfolders are optional. The principle is that feature-owned code
should be close to the feature and should not be spread across global folders.

Boundaries and Imports
----------------------

A feature may use shared core contracts and shared UI primitives. It should
not reach into another feature's internal files. If two features need the
same behavior, first determine whether the behavior is truly shared or whether
the features merely happen to look similar.

A stable shared domain model, such as a ``User`` used by authentication and
profile management, belongs in a shared core model area rather than being
owned by only one of those features. By contrast, a form type or component
specific to profile editing should remain in the profile feature.

This rule prevents hidden coupling between features and makes it possible to
change one feature without unexpectedly changing another.

Routing
-------

Routing is an application concern, but route ownership can remain feature
oriented. A feature defines the routes needed for its screens, while the
application router composes those route definitions into the root route tree.
The root router owns global concerns such as providers, not the internal
business behavior of every feature.

Data Fetching and State
-----------------------

Remote data belongs near the feature that consumes it. Query and mutation
definitions should expose a feature-level API rather than requiring views to
know about request details, serialization, or cache keys. Shared API setup,
clients, authentication, and query configuration can live in core.

A component should express what data it needs through a feature hook or query.
It should not contain unrelated transport code or scattered raw requests.
This keeps caching, loading, error, and invalidation behavior consistent and
makes the data contract easier to test.

UI Composition
--------------

Generic UI primitives are shared infrastructure. Feature components compose
those primitives into product behavior and language. A primitive button,
dialog, or input should not acquire feature-specific rules merely because one
feature currently needs them. Feature wrappers are the appropriate place for
business labels, validation, workflows, and domain-specific composition.

Testing Strategy
----------------

Tests should follow ownership:

* shared core utilities and models have focused unit tests;
* feature hooks test query, mutation, and state behavior;
* feature components test user-visible interaction and rendering;
* views and routes receive integration coverage where they compose several
  pieces;
* end-to-end tests cover important cross-feature workflows.

Co-locating tests with their feature makes the test scope visible and reduces
the chance that a feature change leaves its behavior undocumented.

Applying the Pattern
--------------------

When adding a capability, identify the user-facing feature first. Put its
components, data access, hooks, types, views, route definitions, and tests in
one feature directory. Move code to core only when it has a stable,
cross-feature responsibility. Keep layouts focused on composition and keep
the root router focused on assembly.

A typical application shape is::

   src/
       core/
           api/
           config/
           providers/
           types/
           styles/
       components/ui/
       layouts/
       features/
           <feature-a>/
           <feature-b>/
       router.tsx
       main.tsx

This structure is a guide, not a requirement to create empty folders. The
architectural test is whether related code is easy to find, feature boundaries
are explicit, and shared code has a real shared responsibility.

Relation to kortexa
-------------------

The React frontend follows this architecture with TanStack Router for route
composition, TanStack Query for server-state access, and shadcn for shared UI
primitives. Features own product behavior; ``core`` owns global configuration,
providers, API setup, and genuinely shared models.

Further Reading
---------------

This description is based on *Scalable React Projects with Feature-Based
Architecture* by Naser Rasouli. The article contrasts type-based and
feature-based organization, introduces ``core``, ``layouts``, and ``features``,
and discusses moving domain types to shared code when multiple features need
them.
