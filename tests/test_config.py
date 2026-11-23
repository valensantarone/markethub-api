import pytest
from pydantic import ValidationError

from app.core.config import Settings, get_settings


def test_settings_load_successfully(monkeypatch):
    monkeypatch.setenv("SECRET_KEY", "test-secret-key")
    monkeypatch.setenv("DATABASE_URL", "postgresql://test:test@localhost:5432/test")
    monkeypatch.setenv("ENVIRONMENT", "test")
    
    settings = Settings(_env_file=None)
    
    assert settings.SECRET_KEY == "test-secret-key"
    assert settings.DATABASE_URL == "postgresql://test:test@localhost:5432/test"
    assert settings.ENVIRONMENT == "test"
    assert settings.ACCESS_TOKEN_EXPIRE_MINUTES == 30
    assert settings.REFRESH_TOKEN_EXPIRE_DAYS == 7
    
def test_settings_missing_secret_key_raises_error(monkeypatch):
    monkeypatch.delenv("SECRET_KEY", raising=False)
    monkeypatch.setenv("DATABASE_URL", "postgresql://test:test@localhost:5432/test")
    
    with pytest.raises(ValidationError) as exc_info:
        Settings(_env_file=None)

    assert "SECRET_KEY" in str(exc_info.value)
    
def test_get_settings_is_cached():
    get_settings.cache_clear()
    s1 = get_settings()
    s2 = get_settings()
    
    assert s1 is s2

  

  