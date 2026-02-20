"""Application configuration from environment variables (v6 - Credits)."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment (v6 - Credits)."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Environment (development, staging, production)
    environment: str = "development"

    # Database
    database_url: str = "postgresql+asyncpg://localhost/metering"

    # Redis (required for token metering)
    redis_url: str = ""
    redis_password: str = ""
    redis_max_connections: int = 1000  # Production: 1000 connections

    # SSO/Auth
    sso_url: str = ""
    jwks_cache_ttl: int = 3600  # 1 hour
    token_audience: str = "token-metering-api"  # JWT audience for verification

    # CORS
    allowed_origins: str = "http://localhost:3000"

    # Debug
    debug: bool = False
    log_level: str = "INFO"

    # Dev mode - bypasses auth for local development
    # WARNING: Dev mode should NEVER be enabled in production!
    dev_mode: bool = False
    dev_user_id: str = "dev-user-123"

    # Rate limiting
    rate_limit_requests: int = 100  # Requests per window
    rate_limit_window: int = 60  # Window in seconds
    admin_rate_limit_requests: int = 20  # Stricter limit for admin endpoints

    # Server
    port: int = 8000

    # === Metering Configuration (v6 - Credits) ===

    # Credits per dollar (1 credit = $0.0001)
    credits_per_dollar: int = 10_000

    # Starter credits for new users (~$2.00 budget)
    starter_credits: int = 20_000

    # Inactivity expiry: balance expires after N days of no activity
    inactivity_expiry_days: int = 365

    # Markup percentage on base LLM cost (FR-047)
    markup_percent: float = 20.0

    # Reservation TTL (seconds) - 5 minutes per spec (FR-036)
    reservation_ttl: int = 300

    # Default max output tokens for estimation (FR-068)
    default_max_output_tokens: int = 4096

    # Fail-open behavior (allow requests when Redis is down)
    fail_open: bool = True

    @property
    def allowed_origins_list(self) -> list[str]:
        """Parse comma-separated origins into list."""
        return [origin.strip() for origin in self.allowed_origins.split(",")]


settings = Settings()
