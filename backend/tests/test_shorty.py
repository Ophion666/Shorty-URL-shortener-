from fastapi.testclient import TestClient
from app.main import app
import time
import pytest


client = TestClient(app)

def test_create_link():
    response = client.post(
        "/links/link",
        json = {"original_url": "https://google.com"},
    )

    assert response.status_code == 200
    data = response.json()

    assert "shorty_key" in data
    assert len(data["shorty_key"]) == 6
    assert data["original_url"] == "https://google.com"

def test_redirect_link():
    create_response = client.post(
        "/links/link",
        json = {"original_url": "https://google.com"},
    )

    assert create_response.status_code == 200
    data = create_response.json()

    assert "shorty_key" in data
    assert len(data["shorty_key"]) == 6
    assert data["original_url"] == "https://google.com"

    shorty_key = data["shorty_key"]

    redirect_response = client.get(
        f"/r/{shorty_key}",
        follow_redirects=False
    )

    assert redirect_response.status_code == 307

    assert "Location" in redirect_response.headers

    assert redirect_response.headers["Location"] == "https://google.com"

def test_analytics():
    create_response = client.post(
        "/links/link",
        json = {"original_url": "https://google.com"},
    )

    assert create_response.status_code == 200
    data = create_response.json()

    assert "shorty_key" in data
    assert len(data["shorty_key"]) == 6
    assert data["original_url"] == "https://google.com"

    shorty_key = data["shorty_key"]

    redirect_response = client.get(
        f"/r/{shorty_key}",
        follow_redirects=False,
    )
    redirect_response = client.get(
        f"/r/{shorty_key}",
        follow_redirects=False,
    )

    assert redirect_response.status_code == 307

    assert "Location" in redirect_response.headers

    assert redirect_response.headers["Location"] == "https://google.com"

    analytics_response = client.get(
        f"/links/{shorty_key}/analytics"
    )    

    assert analytics_response.status_code == 200

    data_analytics = analytics_response.json()

    assert data_analytics["click_count"] == 2

    assert len(data_analytics["clicks"]) == 2

    assert data_analytics["clicks"][0]["ip_address"] == "testclient"