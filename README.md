# 💤 Sleep Health Analysis and Classification API

This project delivers a **REST API** that predicts **sleep disorders** (e.g., insomnia, sleep apnea) based on individual lifestyle and health features such as sleep duration, stress level, and physical activity.

🚀 The solution is deployed on **Azure App Service**, with a fully automated **CI/CD pipeline using GitHub Actions**, showcasing a modern MLOps workflow from model training to production.

---

## ⚙️ Technologies Used

- **Python 3.10**
- **FastAPI** – High-performance web framework for APIs
- **scikit-learn** – Random Forest classifier for model training
- **MLflow** – Model tracking and experiment logging
- **Docker** – Containerization of the application
- **GitHub Actions** – Automated testing, Docker build and deployment
- **Azure App Service** – Cloud deployment platform

---

## 📦 API Endpoints

| Endpoint     | Method | Description                                |
|--------------|--------|--------------------------------------------|
| `/predict`   | POST   | Predicts the user's sleep disorder status  |
| `/train`     | POST   | Retrains the model using the base dataset  |
| `/docs`      | GET    | Interactive Swagger UI for API exploration |

---

## 🧪 Automated Testing

**Pytest** is used to validate the API functionality.  
All tests are integrated into the **CI/CD pipeline** and run automatically on each push to the `main` branch.

---

## 🔁 CI/CD and Deployment

- **GitHub Actions** is used to:
  - Install dependencies
  - Run automated tests
  - Build the Docker image
  - **Deploy the API automatically to Azure App Service**

---

## 📊 Model Monitoring

- Each training run is **tracked using MLflow**
- Model metrics, parameters, and artifacts are logged
- The MLflow UI can be launched locally using `mlflow ui`

---

## 🌐 API Demo (if publicly hosted)

🔗 [Live Swagger UI – Hosted on Azure](https://mlsleep-api.azurewebsites.net/docs)  
> *(Replace with your actual deployment URL if needed)*

---

## 📸 Screenshots (Optional)

> *(Add screenshots of Swagger UI, MLflow dashboard, GitHub Actions pipeline, etc.)*

---

## 📁 Project Structure

```bash
mlsleep-api/
│
├── app.py               # FastAPI main application
├── Dockerfile           # Docker image definition
├── requirements.txt     # Project dependencies
├── data/                # Sleep dataset (CSV)
├── tests/               # Pytest unit tests
└── .github/workflows/   # CI/CD GitHub Actions workflow






# 💤 Sleep Health Analysis and Classification API

Ce projet a pour objectif de fournir une **API REST** permettant de **prédire les troubles du sommeil** à partir de données individuelles (âge, sommeil, stress, activité, etc.), en s'appuyant sur un **modèle de machine learning entraîné avec scikit-learn**.

🚀 Déployé sur **Azure App Service** avec une **chaîne CI/CD automatisée via GitHub Actions**, le projet illustre une approche complète MLOps (entraînement, suivi, tests, déploiement).

---

## ⚙️ Technologies utilisées

- **Python 3.10**
- **FastAPI** – API REST rapide et moderne
- **scikit-learn** – Modèle RandomForestClassifier
- **MLflow** – Suivi des runs, métriques et artefacts du modèle
- **Docker** – Conteneurisation de l'API
- **GitHub Actions** – Tests, build Docker et déploiement
- **Azure App Service** – Hébergement cloud de l’API

---

## 📦 Fonctionnalités de l’API

| Endpoint     | Méthode | Description                                       |
|--------------|---------|---------------------------------------------------|
| `/predict`   | POST    | Retourne une prédiction de trouble du sommeil     |
| `/train`     | POST    | Réentraîne le modèle à partir du dataset original |
| `/docs`      | GET     | Interface Swagger auto-générée (FastAPI)          |

---

## 🧪 Tests automatisés

Les **tests unitaires** sont réalisés avec **Pytest** et validés automatiquement via GitHub Actions à chaque push.

---

## 🔁 CI/CD et déploiement

- Pipeline CI/CD via **GitHub Actions**
- Étapes automatisées :
  - Installation des dépendances
  - Exécution des tests
  - Build Docker
  - Déploiement automatique sur Azure App Service

---

## 📊 Monitoring du modèle

- Entraînement loggé automatiquement dans **MLflow**
- Suivi des performances, paramètres et artefacts
- Interface consultable en local via `mlflow ui`

---

## 🔍 Démo API (si déployée en ligne)

🌐 [Lien vers Swagger UI – API déployée sur Azure](https://mlsleep-api.azurewebsites.net/docs)  
> *(à remplacer par ton vrai lien si différent)*

---

## 📸 Aperçus

> *(Ajoute ici des captures ou GIFs illustrant ton Swagger, MLflow, ou pipeline GitHub Actions)*

---

## 📁 Structure du projet

```bash
mlsleep-api/
│
├── app.py               # API FastAPI
├── Dockerfile           # Image Docker
├── requirements.txt     # Dépendances
├── data/                # Dataset CSV
├── tests/               # Tests Pytest
└── .github/workflows/   # Workflow CI/CD GitHub Actions
