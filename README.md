# 🛒 NeuralRetail - AI Sales Intelligence Platform

## 📌 Project Overview

NeuralRetail is an AI-powered retail analytics platform that helps businesses analyze customer behavior, predict customer churn, forecast future sales demand, and optimize inventory management.

The platform uses Machine Learning and Time Series Forecasting techniques to generate actionable business insights through an interactive Streamlit dashboard.

---

## 🚀 Features

### 👥 Customer Segmentation
- RFM (Recency, Frequency, Monetary) Analysis
- K-Means Clustering
- Customer classification into:
  - VIP Customers
  - Regular Customers
  - At Risk Customers

### ⚠️ Churn Prediction
- Random Forest Classifier
- Identification of customers likely to stop purchasing
- Customer retention insights

### 📈 Demand Forecasting
- Facebook Prophet Model
- Future sales prediction
- Time-series demand forecasting

### 📦 Inventory Optimization
- Reorder quantity recommendation
- Inventory planning support
- Demand-driven stock management

### 📊 Interactive Dashboard
- Streamlit-based UI
- Multi-page analytics dashboard
- Real-time visualizations

---

## 🏗️ System Architecture

Dataset
↓
Data Preprocessing
↓
RFM Analysis
↓
Customer Segmentation
↓
Churn Prediction
↓
Demand Forecasting
↓
Inventory Optimization
↓
Streamlit Dashboard

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-Learn
- Prophet
- Joblib
- Streamlit

### Machine Learning Models
- K-Means Clustering
- Random Forest Classifier
- Prophet Forecasting Model

---

## 📂 Project Structure

```text
Neural_Retail
│
├── data
│   ├── Online_Retail.xlsx
│   ├── rfm.csv
│   ├── customer_segments.csv
│   └── forecast.csv
│
├── models
│   ├── segment_model.pkl
│   ├── churn_model.pkl
│   ├── forecast_model.pkl
│   └── scaler.pkl
│
├── pages
│   ├── Home.py
│   ├── Customers.py
│   ├── Churn.py
│   ├── Forecast.py
│   └── Inventory.py
│
├── src
│   ├── preprocess.py
│   ├── segmentation.py
│   ├── churn.py
│   └── forecasting.py
│
├── screenshots
├── app.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

Dataset Used: Online Retail Dataset

Dataset contains:
- Customer ID
- Invoice Information
- Product Information
- Quantity Purchased
- Unit Price
- Purchase Date

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd Neural_Retail
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Dashboard

```bash
streamlit run app.py
```

---

## 📷 Dashboard Screenshots

### Home Dashboard
(Add Screenshot)

### Customer Segmentation
(Add Screenshot)

### Churn Prediction
(Add Screenshot)

### Demand Forecasting
(Add Screenshot)

### Inventory Optimization
(Add Screenshot)

---

## 📈 Results

| Module | Status |
|----------|----------|
| Data Preprocessing | ✅ |
| Customer Segmentation | ✅ |
| Churn Prediction | ✅ |
| Demand Forecasting | ✅ |
| Inventory Optimization | ✅ |
| Interactive Dashboard | ✅ |

---

## 🔮 Future Enhancements

- FastAPI Integration
- Docker Deployment
- MLflow Experiment Tracking
- Cloud Deployment
- Real-Time Prediction APIs
- Advanced Business Analytics

---

## 👨‍💻 Author

**Siddhant Singh**

AI/ML Internship Project

NeuralRetail - AI Sales Intelligence Platform