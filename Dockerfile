FROM python:3.15-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apt update && apt install -y build-essential

COPY  . /app
WORKDIR /app

ENV UV_NO_DEV=1
ENV UV_PYTHON_DOWNLOADS=never

RUN uv sync --locked

FROM python:3.15-slim

RUN groupadd --system --gid 1000 app \
 && useradd --system --uid 1000 --gid app --shell /usr/sbin/nologin app

COPY --from=builder --chown=app:app /app /app

ENV PATH="/app/.venv/bin:$PATH"
# ENV PYTHONPATH="/app"

USER app

WORKDIR /app

CMD ["fastapi", "run", "src/api.py"]
