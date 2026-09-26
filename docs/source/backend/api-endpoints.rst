API / Endpoints
===============

API endpoints are inbound adapters for HTTP. They handle transport-specific
work such as validating request data, choosing status codes, and shaping
response models. They translate an HTTP request into input for a use case and
translate its result into an HTTP response.

Endpoints should not own business rules or persistence behavior. Keeping
those concerns in the application and domain layers means the core does not
need to know that an operation was invoked over HTTP.

In kortexa, ``skills/create_skill/endpoint.py`` uses FastAPI and Pydantic to
define a request model, call the create-skill use case, and return a response.
