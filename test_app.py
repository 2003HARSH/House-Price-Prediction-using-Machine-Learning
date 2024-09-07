from flask import json
from app import app


def test_index_endpoint():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_predict_endpoint():
    test_data = {
        'location': 'Sarjapur',
        'total_sqft': 1200,
        'bath': 2,
        'bhk': 3
    }
    response = app.test_client().post('/predict', json=test_data)
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert 'predicted_price' in response_json
    assert isinstance(response_json['predicted_price'], float)
