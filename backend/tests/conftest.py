"""Shared pytest fixtures."""

import pytest
from fastapi.testclient import TestClient

from kortexa_backend.main import create_app


@pytest.fixture
def client() -> TestClient:
    """Return a test client for a freshly created application."""
    return TestClient(create_app())

