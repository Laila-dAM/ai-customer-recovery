import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base
from app.dependencies import get_db
from main import app


@pytest.fixture
def client():
    test_engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=test_engine,
    )

    Base.metadata.create_all(bind=test_engine)

    def override_get_db():
        db = TestingSessionLocal()

        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=test_engine)
    test_engine.dispose()


def register_user(client):
    return client.post(
        "/auth/register",
        json={
            "company_name": "Test Company",
            "company_email": "company@example.com",
            "company_phone": "61999999999",
            "name": "Test User",
            "email": "user@example.com",
            "password": "StrongPass123",
        },
    )


def test_register_success(client):
    response = register_user(client)

    assert response.status_code == 201
    assert response.json()["email"] == "user@example.com"
    assert response.json()["company_name"] == "Test Company"


def test_login_success(client):
    register_user(client)

    response = client.post(
        "/auth/login",
        json={
            "email": "user@example.com",
            "password": "StrongPass123",
        },
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_wrong_password(client):
    register_user(client)

    response = client.post(
        "/auth/login",
        json={
            "email": "user@example.com",
            "password": "WrongPass123",
        },
    )

    assert response.status_code == 401


def test_login_missing_user(client):
    response = client.post(
        "/auth/login",
        json={
            "email": "unknown@example.com",
            "password": "StrongPass123",
        },
    )

    assert response.status_code == 401


def test_access_protected_route_with_valid_token(client):
    register_user(client)

    login_response = client.post(
        "/auth/login",
        json={
            "email": "user@example.com",
            "password": "StrongPass123",
        },
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.json()["email"] == "user@example.com"
    assert response.json()["role"] == "admin"


def test_access_protected_route_with_invalid_token(client):
    response = client.get(
        "/auth/me",
        headers={"Authorization": "Bearer invalid.token.value"},
    )

    assert response.status_code == 401
