"""Health and readiness endpoints."""

from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/live")
def live() -> dict[str, str]:
    """Report that the process is running."""
    return {"status": "ok"}


@router.get("/ready")
def ready() -> dict[str, str]:
    """Report that the process is ready to receive requests."""
    return {"status": "ok"}

