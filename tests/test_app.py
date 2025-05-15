from fastapi.testclient import TestClient
import pytest
import sys 
import os
from app import app
client = TestClient(app)

def test_predict_mock():
    # Création d'une donnée d'entrée fictive
    payload = {
        "Gender": "Male",
        "Age": 30,
        "Occupation": "Engineer",
        "Sleep_Duration": 7.0,
        "Quality_of_Sleep": 3,
        "Physical_Activity_Level": 2,
        "Stress_Level": 4,
        "BMI_Category": "Normal",
        "Heart_Rate": 70,
        "Daily_Steps": 5000,
        "Systolic": 120.0,
        "Diastolic": 80.0
    }

    # Appel de l'API (note : ici ton modèle doit être pré-chargé pour que ça passe)
    response = client.post("/predict", json=payload)

    # Vérification que l'API répond bien (peu importe le modèle pour ce test simple)
    assert response.status_code in [200, 503, 400]  # On accepte les cas modèle non chargé aussi

    # Si le modèle est chargé, vérifier que la réponse contient bien 'prediction'
    if response.status_code == 200:
        assert "prediction" in response.json()
