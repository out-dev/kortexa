# Python Conventions

Use the existing `src/` layout and type annotations. Manage dependencies with
uv and commit `uv.lock`.

Keep domain code framework-independent. Prefer explicit ports using Python
`Protocol` or abstract base classes. Use Pydantic for transport validation at
API boundaries and translate transport models into application inputs.

Keep tests close to the architectural boundary they verify: domain and
application tests should not require databases, network services, or provider
credentials.
