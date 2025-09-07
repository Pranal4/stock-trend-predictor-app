# QuantumLeap AI - Institutional Trend Forecaster

**Live Application URL:** [https://stock-predictor-api-516063785117.asia-south1.run.app](https://stock-predictor-api-516063785117.asia-south1.run.app)

---

## Overview

This project is a comprehensive, end-to-end machine learning application designed to forecast stock market trends. It demonstrates a full MLOps pipeline, from initial data acquisition and feature engineering to model training, containerization, and final deployment as a scalable, interactive web service on Google Cloud Run.

### Core Features:
* **Dual-Analysis System:** Uses a quantitative XGBoost model for UP/DOWN prediction and the qualitative Gemini LLM for market analysis.
* **Live API Service:** The backend is a FastAPI application, containerized with Docker.
* **Cloud-Native Deployment:** Deployed on Google Cloud Run with an automated cloud build process.
* **Interactive UI:** A sophisticated and responsive single-page web application serves as the project's frontend.

## Technology Stack & Concepts

| Category | Technology/Concept | Purpose |
| :--- | :--- | :--- |
| **Backend & Modeling**| Python 3.9, Pandas, NumPy | Core language for backend and model development. |
| | Scikit-learn | Data manipulation, feature scaling, and baseline modeling. |
| | XGBoost | Advanced gradient boosting model for trend prediction. |
| | Google Gemini API | For generating qualitative, context-aware market analysis. |
| | FastAPI | High-performance web framework for the prediction and analysis API. |
| **Deployment** | Docker | Containerization to package the application into a portable, reproducible container. |
| | Google Cloud Run, Cloud Build | Serverless deployment, automated cloud-native builds, and image storage. |
| **Frontend** | HTML, Tailwind CSS, JavaScript | For creating the interactive and responsive user interface. |
| **Development** | VS Code, Git, GitHub | Code editor, version control, and project workflow. |

## Project Workflow (The 10 Phases)
1.  **Problem Definition:** Framed the task as a binary classification problem to predict the 5-day trend.
2.  **EDA & Feature Engineering:** Acquired raw data from `yfinance`, visualized trends, and engineered predictive features.
3.  **Baseline Modeling:** Trained a Logistic Regression model to establish a baseline performance metric.
4.  **Advanced Modeling:** Trained an XGBoost model and used `GridSearchCV` to find the optimal hyperparameters.
5.  **API Development:** Built a robust API using FastAPI with Pydantic for data validation.
6.  **Containerization:** Created a `Dockerfile` to blueprint the application environment.
7.  **Cloud Deployment:** Deployed the containerized application to Google Cloud Run using the `gcloud` CLI.
8.  **Frontend Development:** Built a sophisticated, single-page web application.
9.  **LLM Integration:** Added a new API endpoint to call the Gemini API for qualitative insights.
10. **Documentation:** Created this README to document the project's architecture, process, and technologies.

---
*This project was developed over a weekend as an intensive, end-to-end mentorship exercise.*













































































































