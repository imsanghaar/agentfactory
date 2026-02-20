"""Application configuration from environment variables."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Environment (development, staging, production)
    environment: str = "development"

    # Database
    database_url: str = "postgresql+asyncpg://localhost/progress"

    # Redis
    redis_url: str = ""
    redis_password: str = ""

    # SSO/Auth
    sso_url: str = ""
    jwks_cache_ttl: int = 3600  # 1 hour
    token_audience: str = "progress-api"

    # CORS
    allowed_origins: str = "http://localhost:3000"

    # Debug
    debug: bool = False
    log_level: str = "INFO"

    # Dev mode - bypasses auth for local development
    dev_mode: bool = False
    dev_user_id: str = "dev-user-123"

    # Server
    port: int = 8002

    # Cache TTLs (seconds)
    cache_ttl_progress: int = 300
    cache_ttl_leaderboard: int = 300

    @property
    def allowed_origins_list(self) -> list[str]:
        """Parse comma-separated origins into list."""
        return [origin.strip() for origin in self.allowed_origins.split(",")]


settings = Settings()
