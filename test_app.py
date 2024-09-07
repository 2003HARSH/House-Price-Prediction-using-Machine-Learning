from flask import json
from app import app


def test_index_endpoint(client):
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_predict_endpoint(client):
    test_data = {
        'location': '1st Phase JP Nagar',
        'total_sqft': 1200,
        'bath': 2,
        'bhk': 3
    }
    response = app.test_client().post('/predict', json=test_data)
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert 'predicted_price' in response_json
    assert isinstance(response_json['predicted_price'], float)
