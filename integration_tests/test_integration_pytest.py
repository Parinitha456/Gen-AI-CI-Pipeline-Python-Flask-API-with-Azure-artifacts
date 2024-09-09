import pytest
from app import create_app
import json

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_post_data(client):
    """Test POST request integration with a simple JSON payload."""
    payload = {'key': 'value'}
    response = client.post('/api/data', data=json.dumps(payload), content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'success'
    assert data['data']['key'] == 'value'
