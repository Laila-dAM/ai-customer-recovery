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


def create_authenticated_user(client, suffix="first"):
    response = client.post(
        "/auth/register",
        json={
            "company_name": f"Company {suffix}",
            "company_email": f"company-{suffix}@example.com",
            "name": f"User {suffix}",
            "email": f"user-{suffix}@example.com",
            "password": "StrongPass123",
        },
    )

    assert response.status_code == 201

    login_response = client.post(
        "/auth/login",
        json={
            "email": f"user-{suffix}@example.com",
            "password": "StrongPass123",
        },
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    return {"Authorization": f"Bearer {token}"}


def test_create_lead(client):
    headers = create_authenticated_user(client)

    response = client.post(
        "/leads",
        headers=headers,
        json={
            "name": "Maria Silva",
            "email": "MARIA@EXAMPLE.COM",
            "phone": "61999999999",
        },
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Maria Silva"
    assert response.json()["email"] == "maria@example.com"
    assert response.json()["status"] == "new"


def test_list_leads_and_filter_by_status(client):
    headers = create_authenticated_user(client)

    client.post(
        "/leads",
        headers=headers,
        json={"name": "Maria Silva", "status": "new"},
    )

    client.post(
        "/leads",
        headers=headers,
        json={"name": "João Santos", "status": "interested"},
    )

    response = client.get("/leads?status=interested", headers=headers)

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "João Santos"


def test_get_and_update_lead(client):
    headers = create_authenticated_user(client)

    create_response = client.post(
        "/leads",
        headers=headers,
        json={"name": "Maria Silva"},
    )

    lead_id = create_response.json()["id"]

    get_response = client.get(f"/leads/{lead_id}", headers=headers)

    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Maria Silva"

    update_response = client.patch(
        f"/leads/{lead_id}",
        headers=headers,
        json={
            "name": "Maria Oliveira",
            "status": "interested",
        },
    )

    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Maria Oliveira"
    assert update_response.json()["status"] == "interested"


def test_delete_lead(client):
    headers = create_authenticated_user(client)

    create_response = client.post(
        "/leads",
        headers=headers,
        json={"name": "Maria Silva"},
    )

    lead_id = create_response.json()["id"]

    delete_response = client.delete(
        f"/leads/{lead_id}",
        headers=headers,
    )

    assert delete_response.status_code == 204

    get_response = client.get(f"/leads/{lead_id}", headers=headers)

    assert get_response.status_code == 404


def test_company_cannot_access_another_company_lead(client):
    first_headers = create_authenticated_user(client, "first")
    second_headers = create_authenticated_user(client, "second")

    create_response = client.post(
        "/leads",
        headers=first_headers,
        json={"name": "Private Lead"},
    )

    lead_id = create_response.json()["id"]

    response = client.get(
        f"/leads/{lead_id}",
        headers=second_headers,
    )

    assert response.status_code == 404


def test_leads_require_authentication(client):
    response = client.get("/leads")

    assert response.status_code == 401


def test_create_lead_rejects_invalid_status(client):
    headers = create_authenticated_user(client)

    response = client.post(
        "/leads",
        headers=headers,
        json={
            "name": "Maria Silva",
            "status": "invalid",
        },
    )

    assert response.status_code == 422
