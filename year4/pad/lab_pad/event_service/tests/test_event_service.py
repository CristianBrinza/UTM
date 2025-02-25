import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_event(client):
    response = client.post('/events/create', json={
        'title': 'Meeting',
        'description': 'Team sync',
        'date': '2024-10-26'
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Event created successfully'
