FROM python:3.12.9 AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
WORKDIR /app


RUN python -m venv .venv
COPY requirements.txt ./
RUN .venv/bin/pip install -r requirements.txt
FROM python:3.12.9-slim
WORKDIR /app
ENV PORT=8080
COPY --from=builder /app/.venv .venv/
COPY . .
CMD ["/app/.venv/bin/python", "-m", "markify.app"]
