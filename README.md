# Machine Learning Infrastructure for EUR/USD Trade Automation

## Overview

Distributed machine learning infrastructure for EUR/USD forecasting, automated trade execution, and real-time prediction serving using Python, Docker, Kubernetes, and REST APIs.

This project explores the development of a modular machine learning-driven trading system capable of training forecasting models, serving live predictions, and executing automated trades through an integrated execution engine.

---

# Features

* GRU-based time-series forecasting pipeline
* Automated trade execution engine
* REST API prediction serving
* Dockerized microservices architecture
* Kubernetes deployment support (GKE)
* Real-time trailing stop-loss management
* Hyperparameter tuning workflows
* Telegram alert integration
* Modular training and inference pipelines
* Multi-service communication using Docker Compose

---

# System Architecture

```text
Market Data
     ↓
Training Pipeline
     ↓
Trained Model
     ↓
REST API Prediction Service
     ↓
Trade Execution Engine
     ↓
MetaTrader Integration
     ↓
Trade Monitoring & Telegram Alerts
```

---

# Tech Stack

## Backend

* Python

## Machine Learning

* TensorFlow / Keras
* NumPy
* Pandas

## Infrastructure

* Docker
* Docker Compose
* Kubernetes (GKE)

## APIs & Automation

* REST API
* Telegram Bot API

## Trading Integration

* MetaTrader 5

---

# Project Structure

```bash
├── training/
├── models/
├── rest_api/
├── trade_execution/
├── hyperparameter_tuning/
├── docker-compose.yml
├── Kubernetes.yaml
├── telegram.py
├── requirements.txt
└── settings.json
```

## Folder Descriptions

### training/

Contains machine learning training scripts and preprocessing workflows for financial time-series forecasting.

### models/

Stores trained machine learning models and serialized model artifacts.

### rest_api/

REST API services responsible for serving live predictions to the execution engine.

### trade_execution/

Handles automated trade execution logic, order management, and trailing stop-loss operations.

### hyperparameter_tuning/

Contains scripts and experiments for optimizing GRU model configurations and parameters.

### telegram.py

Notification and monitoring integration using Telegram Bot API.

### docker-compose.yml

Defines containerized multi-service orchestration.

### Kubernetes.yaml

Deployment configuration for Kubernetes clusters on Google Kubernetes Engine (GKE).

---

# Installation

## Clone Repository

```bash
git clone https://github.com/pizzyander/Machine-Learning-Expert-Advisor-for-EURUSD.git

cd Machine-Learning-Expert-Advisor-for-EURUSD
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Local Development

```bash
python training/train.py
```

## Run API Service

```bash
python rest_api/app.py
```

## Run Trade Execution Engine

```bash
python trade_execution/executor.py
```

---

# Docker Deployment

## Build and Run Containers

```bash
docker-compose up --build
```

This initializes:

* Training services
* Prediction API
* Trade execution services
* Internal container networking

---

# Kubernetes Deployment

## Deploy to GKE

```bash
kubectl apply -f Kubernetes.yaml
```

The application supports deployment using Kubernetes clusters for scalable container orchestration.

---

# Workflow

1. Market data is collected and preprocessed.
2. GRU-based models are trained using time-series forecasting techniques.
3. Trained models are served through REST API endpoints.
4. Trade execution services consume prediction outputs.
5. Orders are managed and monitored automatically.
6. Telegram notifications provide execution and monitoring updates.

---

# Model Training

The training pipeline focuses on financial time-series forecasting for EUR/USD market data using recurrent neural network architectures.

## Current Areas of Experimentation

* Feature engineering
* Indicator optimization
* Hyperparameter tuning
* Sequence modeling using GRU networks
* Prediction confidence evaluation
* Trade execution timing

## Challenges

Financial market prediction remains highly complex due to:

* Market volatility
* Noise in time-series data
* Risk of overfitting
* Slippage and execution latency
* Regime changes in market behavior

---

# Deployment & Infrastructure

The project is structured as a modular distributed system with separate components for:

* Model training
* Prediction serving
* Automated execution
* Monitoring and notifications

Infrastructure features include:

* Docker containerization
* Docker Compose orchestration
* Kubernetes deployment support
* Scalable service architecture
* Container networking

---

# Challenges & Lessons Learned

During development, several engineering and machine learning challenges were encountered:

* Avoiding overfitting in financial forecasting models
* Managing communication between distributed services
* Maintaining stable containerized environments
* Handling latency between prediction generation and trade execution
* Improving prediction generalization across varying market conditions
* Structuring scalable ML workflows for experimentation and deployment

---

# Future Improvements

Planned improvements include:

* Experiment tracking with MLflow
* CI/CD pipeline integration
* Advanced feature engineering
* Market regime classification
* Centralized logging and observability
* Reinforcement learning experimentation
* Enhanced risk management systems
* Real-time monitoring dashboards

---

# Disclaimer

This project is intended for educational and research purposes only and does not constitute financial advice.

Trading financial markets involves significant risk, and no guarantee of profitability is implied.

---

# Author

Developed by Akinfe Adesanmi Thomas.
