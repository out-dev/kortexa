"""HTTP API tests."""

from fastapi import FastAPI
from fastapi.testclient import TestClient


def test_create_app_returns_fastapi_application(client: TestClient) -> None:
    assert isinstance(client.app, FastAPI)


def test_live_endpoint(client: TestClient) -> None:
    response = client.get("/api/v1/health/live")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ready_endpoint(client: TestClient) -> None:
    response = client.get("/api/v1/health/ready")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_unversioned_health_endpoints_are_not_available(client: TestClient) -> None:
    assert client.get("/health/live").status_code == 404
    assert client.get("/health/ready").status_code == 404


def test_openapi_contains_only_versioned_health_paths(client: TestClient) -> None:
    paths = client.get("/openapi.json").json()["paths"]

    assert "/api/v1/health/live" in paths
    assert "/api/v1/health/ready" in paths
    assert "/health/live" not in paths
    assert "/health/ready" not in paths


def test_cors_allows_configured_frontend_origin(client: TestClient) -> None:
    response = client.get(
        "/api/v1/health/live",
        headers={"Origin": "http://localhost:5173"},
    )

    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "http://localhost:5173"
