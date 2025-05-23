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





