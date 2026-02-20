# =============================================================================
# Progress API - Production Dockerfile (Hardened)
# Multi-stage build | Non-root | Minimal attack surface | OCI compliant
# Based on study-mode-api pattern
# =============================================================================

ARG PYTHON_VERSION=3.12

# -----------------------------------------------------------------------------
# Stage 1: Builder - Compile dependencies with build tools
# -----------------------------------------------------------------------------
FROM python:${PYTHON_VERSION}-slim AS builder

# Install build dependencies for native packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    libffi-dev && \
    rm -rf /var/lib/apt/lists/*

# Install uv from official image (only in builder)
COPY --from=ghcr.io/astral-sh/uv:0.5 /uv /usr/local/bin/uv

WORKDIR /build

# Copy project files (hatchling needs README.md + src/ to build the wheel)
COPY pyproject.toml README.md ./
COPY src/ ./src/

# Install dependencies into isolated venv
RUN uv venv /app/.venv && \
    . /app/.venv/bin/activate && \
    uv pip install . --compile-bytecode

# -----------------------------------------------------------------------------
# Stage 2: Production Runtime (NO uv, NO build tools)
# -----------------------------------------------------------------------------
FROM python:${PYTHON_VERSION}-slim

LABEL org.opencontainers.image.title="Progress API" \
      org.opencontainers.image.description="Gamification and progress tracking service" \
      org.opencontainers.image.vendor="Panaversity" \
      org.opencontainers.image.source="https://github.com/panaversity/agentfactory"

# Install ONLY runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq5 && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Create non-root user (k8s runAsNonRoot compatible)
RUN groupadd --gid 10001 app && \
    useradd --uid 10001 --gid 10001 --shell /sbin/nologin --no-create-home --no-log-init app

WORKDIR /app

# Copy ONLY the venv from builder (uv stays in builder)
COPY --from=builder --chown=app:app /app/.venv /app/.venv

# Copy application source
COPY --chown=app:app src/ ./src/

# Environment configuration
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH="/app/src" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8002

# Switch to non-root user
USER app

EXPOSE 8002

# Health check using Python stdlib (no curl needed)
HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8002/health', timeout=3)" || exit 1

STOPSIGNAL SIGTERM

# Production uvicorn (single worker - scale with k8s replicas)
CMD ["sh", "-c", "exec uvicorn progress_api.main:app \
    --host 0.0.0.0 \
    --port ${PORT} \
    --proxy-headers \
    --forwarded-allow-ips '*' \
    --no-access-log"]
