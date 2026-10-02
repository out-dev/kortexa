FROM ghcr.io/astral-sh/uv:0.12.13 AS uv
FROM python:3.12-slim

COPY --from=uv /uv /uvx /bin/

RUN useradd --create-home --uid 10001 app \
    && mkdir /app \
    && chown app:app /app

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY --chown=app:app manage.py ./
COPY --chown=app:app src ./src

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH="/app/src" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

USER app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
