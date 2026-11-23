from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
    
    # Entorno de ejecución
    ENVIRONMENT: Literal["development", "staging", "production", "test"] = "development"
    
    # Base de datos
    DATABASE_URL: str
    
    # Seguridad / JWT
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
@lru_cache
def get_settings() -> Settings:
    return Settings()