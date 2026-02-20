"""Prometheus metrics for observability."""

from prometheus_client import Counter, Histogram, Info

# Service info
SERVICE_INFO = Info("token_metering", "Token Metering API service information")
SERVICE_INFO.info({"version": "1.0.0", "service": "token-metering-api"})

# Request latency histograms
METERING_CHECK_LATENCY = Histogram(
    "metering_check_latency_seconds",
    "Latency of balance check (reservation) requests",
    ["status"],
    buckets=[0.001, 0.002, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0],
)

METERING_DEDUCT_LATENCY = Histogram(
    "metering_deduct_latency_seconds",
    "Latency of token deduction (finalize) requests",
    ["status"],
    buckets=[0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5],
)

METERING_RELEASE_LATENCY = Histogram(
    "metering_release_latency_seconds",
    "Latency of reservation release requests",
    ["status"],
    buckets=[0.001, 0.002, 0.005, 0.01, 0.025, 0.05, 0.1],
)

# Request counters
METERING_REQUESTS_TOTAL = Counter(
    "metering_requests_total",
    "Total metering requests by operation and status",
    ["operation", "status"],
)

METERING_REJECTED_TOTAL = Counter(
    "metering_rejected_total",
    "Total rejected requests by reason",
    ["reason"],
)

# Balance tracking
NEGATIVE_BALANCE_TOTAL = Counter(
    "metering_negative_balances_total",
    "Total accounts that went negative",
)

RESERVATIONS_EXPIRED_TOTAL = Counter(
    "metering_reservations_expired_total",
    "Total reservations that expired without finalize/release",
)

# Redis health
REDIS_ERRORS_TOTAL = Counter(
    "metering_redis_errors_total",
    "Total Redis operation errors",
    ["operation"],
)

REDIS_FAILOPEN_TOTAL = Counter(
    "metering_redis_failopen_total",
    "Total requests that used fail-open mode",
)

# Database health
DB_ERRORS_TOTAL = Counter(
    "metering_db_errors_total",
    "Total database operation errors",
    ["operation"],
)


def track_check_request(status: str, latency: float) -> None:
    """Track a balance check request."""
    METERING_CHECK_LATENCY.labels(status=status).observe(latency)
    METERING_REQUESTS_TOTAL.labels(operation="check", status=status).inc()


def track_deduct_request(status: str, latency: float) -> None:
    """Track a token deduction request."""
    METERING_DEDUCT_LATENCY.labels(status=status).observe(latency)
    METERING_REQUESTS_TOTAL.labels(operation="deduct", status=status).inc()


def track_release_request(status: str, latency: float) -> None:
    """Track a reservation release request."""
    METERING_RELEASE_LATENCY.labels(status=status).observe(latency)
    METERING_REQUESTS_TOTAL.labels(operation="release", status=status).inc()


def track_rejection(reason: str) -> None:
    """Track a rejected request."""
    METERING_REJECTED_TOTAL.labels(reason=reason).inc()


def track_negative_balance() -> None:
    """Track an account going negative."""
    NEGATIVE_BALANCE_TOTAL.inc()


def track_expired_reservation() -> None:
    """Track an expired reservation."""
    RESERVATIONS_EXPIRED_TOTAL.inc()


def track_redis_error(operation: str) -> None:
    """Track a Redis error."""
    REDIS_ERRORS_TOTAL.labels(operation=operation).inc()


def track_failopen() -> None:
    """Track fail-open usage."""
    REDIS_FAILOPEN_TOTAL.inc()


def track_db_error(operation: str) -> None:
    """Track a database error."""
    DB_ERRORS_TOTAL.labels(operation=operation).inc()
