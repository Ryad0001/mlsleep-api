import streamlit as st
import requests

# URL de ton API FastAPI (déployée sur Azure)
API_URL = "https://mlsleepapi4-e6b7hhdzh0b9bjbt.francecentral-01.azurewebsites.net/docs#/default/train_train_post"

st.title("Prédiction des troubles du sommeil 💤")

st.write("Remplis les informations ci-dessous pour recevoir une prédiction.")

# Formulaire utilisateur
age = st.slider("Âge", 10, 100, 25)
sleep_duration = st.slider("Durée de sommeil (heures)", 0, 12, 7)
stress_level = st.slider("Niveau de stress (1 à 10)", 1, 10, 5)
physical_activity_level = st.slider("Activité physique (1 à 10)", 1, 10, 5)
bmi_category = st.selectbox("Catégorie IMC", ["Normal", "Overweight", "Obese", "Underweight"])
blood_pressure = st.selectbox("Tension artérielle", ["Normal", "High", "Low"])
heart_rate = st.number_input("Fréquence cardiaque", 40, 150, 70)

# Appel API
if st.button("Prédire"):
    data = {
        "Age": age,
        "Sleep Duration": sleep_duration,
        "Stress Level": stress_level,
        "Physical Activity Level": physical_activity_level,
        "BMI Category": bmi_category,
        "Blood Pressure": blood_pressure,
        "Heart Rate": heart_rate
    }

    try:
        response = requests.get(API_URL, json=data)
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            st.success(f"Trouble prédit : {prediction}")
        else:
            st.error(f"Erreur {response.status_code} : {response.text}")
    except Exception as e:
        st.error(f"Erreur lors de la communication avec l’API : {e}")
