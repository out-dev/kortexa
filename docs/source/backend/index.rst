Backend
=======

Organize the application by **vertical features/use cases**, while applying **Hexagonal Architecture** inside each 
feature to separate domain logic, ports, and adapters. 
Use FastAPI `Depends` only at the outer boundary for wiring, keeping domain and use-case code independent of 
FastAPI, databases, and infrastructure.

Project Structure
=================

The current backend project is organized as follows. The linked entries open
the guide for each architectural element.

.. code-block:: text

   backend/
   ├── src/
   │   ├── main.py
   │   └── skills/ :doc:`Business Features <business_feature>`
   │       ├── domain/
   │       ├── ports/
   │       ├── adapters/
   │       └── create_skill/
   ├── tests/
   └── pyproject.toml

.. toctree::
 :hidden:
 :maxdepth: 1

 business_feature
 domain
 application
 ports
 adapters
 api-endpoints
 dependencies-wiring

Development
===========

Install the backend and its development tools with::

   uv sync
   uv run pytest
   uv run ruff check .
   uv run uvicorn main:app --reload
