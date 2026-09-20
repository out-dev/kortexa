"""Configuration tests."""

from kortexa_backend.infrastructure.config import Settings


def test_settings_have_safe_defaults() -> None:
    settings = Settings()

    assert settings.app_name == "kortexa backend API"
    assert settings.environment == "development"
    assert settings.cors_origins == ["http://localhost:5173"]


def test_settings_support_environment_overrides(monkeypatch) -> None:
    monkeypatch.setenv("KORTEXA_APP_NAME", "test API")
    monkeypatch.setenv("KORTEXA_ENVIRONMENT", "test")

    settings = Settings()

    assert settings.app_name == "test API"
    assert settings.environment == "test"


def test_settings_support_cors_origin_overrides(monkeypatch) -> None:
    monkeypatch.setenv("KORTEXA_CORS_ORIGINS", '["http://localhost:4173"]')

    settings = Settings()

    assert settings.cors_origins == ["http://localhost:4173"]
