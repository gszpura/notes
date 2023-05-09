from enum import Enum
from pydantic import BaseSettings


class AppEnvironment(str, Enum):
    PRODUCTION = "production"
    DEV = "development"
    TESTING = "testing"


class Config(BaseSettings):
    """
    Base configuration.
    """

    API_V1_STR = "/api/v1"

    APP_VERSION: str = "v1"
    FASTAPI_ENV: AppEnvironment = AppEnvironment.DEV

    UVICORN_HOST: str = "0.0.0.0"
    UVICORN_PORT: int = 8000

    PROJECT_NAME: str | None = "FastAPI app template"

    DATABASE_USER: str = "app"
    DATABASE_PASSWORD: str = "password"
    DATABASE_URL: str = "127.0.0.1"
    DATABASE_NAME: str = "app"
    DATABASE_PORT: int = 5432
    DATABASE_POOL_SIZE: int = 5
    DATABASE_MAX_OVERFLOW: int = 10

    BACKEND_CORS_ORIGINS = "http://localhost:3000"

    def is_dev(self) -> bool:
        return self.FASTAPI_ENV == AppEnvironment.DEV

    def is_prod(self) -> bool:
        return self.FASTAPI_ENV == AppEnvironment.PRODUCTION


settings = Config(_env_file=".env", _env_file_encoding="utf-8")
