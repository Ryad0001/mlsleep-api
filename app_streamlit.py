import streamlit as st
import requests
import time

# --- URLs de l'API déployée sur Azure
API_PREDICT_URL = "https://mlsleepapi4-e6b7hhdzh0b9bjbt.francecentral-01.azurewebsites.net/predict"
API_TRAIN_URL = "https://mlsleepapi4-e6b7hhdzh0b9bjbt.francecentral-01.azurewebsites.net/train"

# --- Initialisation automatique : entraînement du modèle ---
@st.cache_resource(show_spinner=False)
def initialize_model():
    try:
        response = requests.post(API_TRAIN_URL)
        if response.status_code == 200:
            st.info("✅ Modèle entraîné automatiquement.")
        else:
            st.warning(f"⚠️ Entraînement échoué : {response.text}")
    except Exception as e:
        st.error(f"Erreur lors de l’entraînement automatique : {e}")

# --- Titre
st.title("Prédiction des troubles du sommeil 💤")

# --- Lancer l'entraînement automatique
initialize_model()


def is_model_ready():
    try:
        r = requests.get("https://mlsleepapi4-e6b7hhdzh0b9bjbt.francecentral-01.azurewebsites.net/status")
        return r.status_code == 200 and r.json().get("status") == "ready"
    except:
        return False

# Attendre que le modèle soit prêt
with st.spinner("⏳ Initialisation du modèle..."):
    timeout = 30  # secondes max d'attente
    start = time.time()
    while not is_model_ready():
        time.sleep(2)
        if time.time() - start > timeout:
            st.error("❌ Délai dépassé. Le modèle n’a pas pu être chargé.")
            st.stop()
    st.success("✅ Modèle chargé, tu peux lancer une prédiction.")


st.write("Remplis les informations ci-dessous pour recevoir une prédiction.")

# --- Formulaire utilisateur
gender = st.selectbox("Genre", ["Male", "Female", "Other"])
age = st.slider("Âge", 10, 100, 25)
occupation = st.selectbox("Profession", ["Student", "Employee", "Self-employed", "Unemployed", "Other"])
sleep_duration = st.slider("Durée de sommeil (heures)", 0.0, 12.0, 7.0, step=0.5)
quality_of_sleep = st.slider("Qualité du sommeil (1 à 10)", 1, 10, 6)
physical_activity_level = st.slider("Activité physique (1 à 10)", 1, 10, 5)
stress_level = st.slider("Niveau de stress (1 à 10)", 1, 10, 5)
bmi_category = st.selectbox("Catégorie IMC", ["Normal", "Overweight", "Obese", "Underweight"])
blood_pressure = st.selectbox("Tension artérielle", ["Normal", "High", "Low"])
heart_rate = st.number_input("Fréquence cardiaque", 40, 150, 70)
daily_steps = st.number_input("Nombre de pas quotidiens", 0, 30000, 5000)
systolic = st.number_input("Tension systolique", 80, 200, 120)
diastolic = st.number_input("Tension diastolique", 40, 120, 80)

# --- Appel API pour prédiction
if st.button("Prédire"):
    data = {
        "Gender": gender,
        "Age": age,
        "Occupation": occupation,
        "Sleep_Duration": sleep_duration,
        "Quality_of_Sleep": quality_of_sleep,
        "Physical_Activity_Level": physical_activity_level,
        "Stress_Level": stress_level,
        "BMI_Category": bmi_category,
        "Blood_Pressure": blood_pressure,
        "Heart_Rate": heart_rate,
        "Daily_Steps": daily_steps,
        "Systolic": systolic,
        "Diastolic": diastolic
    }

    try:
        response = requests.post(API_PREDICT_URL, json=data)
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            st.success(f"🧠 Trouble prédit : {prediction}")
        else:
            st.error(f"Erreur {response.status_code} : {response.text}")
    except Exception as e:
        st.error(f"Erreur lors de la communication avec l’API : {e}")
