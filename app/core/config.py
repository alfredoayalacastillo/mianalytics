import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "MIANALITICS"
    ENVIRONMENT: str = "development"
    PORT: int = 8000
    LOG_LEVEL: str = "info"
    INTERNAL_API_KEY: str = "mianalytics-secret-key-change-in-production"
    
    # PostgreSQL & pgvector settings
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/corteza"
    POSTGRES_READ_ONLY: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
