import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['service'] == 'URL Shortener API'

def test_shorten_url(client):
    response = client.post('/api/shorten', json={"url": "https://example.com"})
    assert response.status_code == 200
    data = response.get_json()
    assert "short_code" in data
    assert "short_url" in data

def test_redirect_existing_short_code(client):
    # Step 1: Shorten a URL
    response = client.post('/api/shorten', json={"url": "https://example.com"})
    short_code = response.get_json()["short_code"]

    # Step 2: Hit the short URL
    response = client.get(f'/{short_code}', follow_redirects=False)
    assert response.status_code == 302
    assert response.headers["Location"] == "https://example.com"
def test_redirect_invalid_short_code(client):
    response = client.get("/invalid123")
    assert response.status_code == 404
def test_analytics_endpoint(client):
    # Shorten a URL
    response = client.post('/api/shorten', json={"url": "https://example.com"})
    short_code = response.get_json()["short_code"]

    # Trigger a redirect to increment click count
    client.get(f'/{short_code}')

    # Check stats
    response = client.get(f'/api/stats/{short_code}')
    data = response.get_json()

    assert response.status_code == 200
    assert data["url"] == "https://example.com"
    assert isinstance(data["clicks"], int)
    assert data["clicks"] >= 1
    assert "created_at" in data
