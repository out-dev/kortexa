HTMX UI
=======

The browser UI is a server-rendered interface in the FastAPI application.
HTMX enhances ordinary HTML links and forms with partial updates; it does not
own business behavior or introduce a separate frontend application.

Architecture
------------

Treat page and fragment handlers as inbound HTTP adapters. They validate
request data, invoke the same feature use cases as the JSON API, and render
HTML. Keep domain logic, application use cases, ports, and infrastructure
adapters independent of FastAPI, Jinja2, and HTMX. Keep JSON API routes and
HTML UI routes separate so their response contracts remain explicit.

Organize UI handlers within their vertical feature, next to the corresponding
use case and API endpoint. Shared template configuration and static assets
belong at the application boundary; templates can be grouped by feature:

.. code-block:: text

   backend/
   ├── src/
   │   ├── main.py
   │   ├── web/
   │   │   ├── templates.py
   │   │   └── static/
   │   │       ├── htmx.min.js
   │   │       └── app.css
   │   └── skills/
   │       ├── domain/
   │       ├── ports/
   │       ├── adapters/
   │       ├── create_skill/
   │       │   ├── use_case.py
   │       │   ├── endpoint.py
   │       │   └── ui_endpoint.py
   │       └── list_skills/
   │           ├── use_case.py
   │           ├── endpoint.py
   │           └── ui_endpoint.py
   └── templates/
       ├── base.html
       └── skills/
           ├── list.html
           ├── _skill_list.html
           └── _skill_form.html

Keep the existing API route contract. Mount browser routes under a distinct
prefix such as ``/ui``. A page route renders the full document; HTMX
interactions return only the fragment targeted for replacement. For
progressive enhancement, forms should still submit and render useful HTML
without JavaScript. Validation errors should render in the relevant form
fragment, and successful updates should replace only the affected region.

Templates should contain presentation and HTMX attributes only. They must
not call repositories, enforce business rules, or construct domain objects.
Both API and UI handlers should use the feature's existing application
use cases and dependency wiring.

Authentication and assets
-------------------------

Protect full-page and fragment routes consistently using authentication and
authorization at the HTTP boundary. Browser authentication must be suitable
for same-origin HTML requests; do not expose identity tokens to client-side
JavaScript. If authentication uses cookies, protect state-changing requests
against CSRF.

HTMX is a browser JavaScript asset, not a Python dependency. Serve a pinned
HTMX release as a local static asset rather than adding a frontend build
pipeline. Jinja2 renders templates, and ``python-multipart`` supports HTML
form parsing. These are backend runtime dependencies.

Initial slice
-------------

Start with one feature page that covers the whole interaction: render a list,
submit a create form, show validation errors, and update the list fragment on
success. This validates the page/fragment boundary and shared use-case path
before expanding the UI to other features.
