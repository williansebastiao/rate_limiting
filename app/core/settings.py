from pydantic import RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "Rate Limiter"
    APP_VERSION: str = "1.0.0"
    APP_ENV: str = "prd"
    APP_PATH: str = "/api"

    RATE_LIMIT: int = 100
    CACHE_TIME: int = 60

    CACHE_DRIVER: RedisDsn

    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=".env",
    )


settings = Settings()
