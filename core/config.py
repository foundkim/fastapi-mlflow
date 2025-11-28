"""Configuration module for FastAPI application."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Configuration settings for the FastAPI application."""

    MLFLOW_TRACKING_URI: str = "http://localhost:5000"
    MLFLOW_MODEL_URI: str

    APP_NAME: str = "FastAPI MFlow Application"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "A FastAPI application for MFlow integration"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    LOG_LEVEL: str = "INFO"


config = Config()
