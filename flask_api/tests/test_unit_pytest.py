import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test if homepage is accessible."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Flask API" in response.data
