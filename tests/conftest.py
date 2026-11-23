import pytest

@pytest.fixture(autouse=True)
def set_test_env(monkeypatch):
    monkeypatch.setenv("SECRET_KEY", "super-secret-key-for-testing-only-12345")
    monkeypatch.setenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/test_db")