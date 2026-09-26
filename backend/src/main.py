from fastapi import FastAPI

from skills.create_skill.endpoint import router as create_skill_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Skills API",
        version="1.0.0",
    )
    # Include skill-related routers
    app.include_router(create_skill_router, prefix="/skills")

    return app


app = create_app()


def main() -> None:
    create_app()