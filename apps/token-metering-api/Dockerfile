# Token Metering API Dockerfile
# Multi-stage build for minimal production image

FROM python:3.12-slim as builder

WORKDIR /app

# Install uv for faster package installation
RUN pip install --no-cache-dir uv

# Copy dependency files and source code
COPY pyproject.toml README.md ./
COPY src/ ./src/

# Install package (builds wheel via hatchling, installs into site-packages)
RUN uv pip install --system --no-cache .

# Production stage
FROM python:3.12-slim as production

WORKDIR /app

# Create non-root user
RUN useradd --create-home --shell /bin/bash appuser

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
# v5 uses SQLModel with auto-create - no migrations needed
# Lua scripts are inside src/token_metering_api/scripts/
COPY src/ ./src/

# Set ownership
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PORT=8000

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import httpx; httpx.get('http://localhost:${PORT}/health')" || exit 1

# Run with uvicorn (shell form so $PORT is expanded at runtime)
CMD uvicorn token_metering_api.main:app --host 0.0.0.0 --port $PORT
