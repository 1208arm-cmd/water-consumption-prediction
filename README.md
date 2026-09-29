# 💧 Water Consumption Prediction

A Machine Learning-based web application that predicts daily household water consumption using weather conditions and the number of residents. The project is built with **Python, Flask, Scikit-learn, Bootstrap 5, and Chart.js**.

---

## 📌 Project Overview

The system predicts the estimated daily water consumption (in liters) based on:

- 📅 Date
- 📆 Day
- 🌤 Season
- 🌡 Temperature
- 💧 Humidity
- 🌧 Rainfall
- 👨‍👩‍👧 Number of Residents

The prediction model uses the **Random Forest Regressor** algorithm trained on a dataset of **500 records**.

---

## ✨ Features

- 💧 Water Consumption Prediction
- 🤖 Machine Learning (Random Forest Regressor)
- 🌐 Flask Web Application
- 📊 Interactive Dashboard
- 📈 Monthly Water Consumption Chart
- 🌡 Temperature vs Water Consumption Graph
- 🌧 Rainfall vs Water Consumption Graph
- 🥧 Water Usage Distribution Pie Chart
- 📋 Prediction History
- 📄 Download Prediction Report as PDF
- 📈 Model Accuracy Display
- 📱 Responsive Bootstrap 5 Interface

---

## 🛠 Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- ReportLab
- Bootstrap 5
- Chart.js
- HTML5
- CSS3
- JavaScript

---

## 📂 Project Structure

```
Water_Consumption_Prediction/
│
├── app.py
├── train_model.py
├── generate_dataset.py
├── dataset.csv
├── prediction_history.csv
├── model.pkl
├── accuracy.pkl
├── day_encoder.pkl
├── season_encoder.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── chart.js
│   └── images/
│
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Water_Consumption_Prediction.git
```

```bash
cd Water_Consumption_Prediction
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install flask pandas scikit-learn joblib reportlab matplotlib
```

---

## ▶ Generate Dataset (Optional)

```bash
python generate_dataset.py
```

---

## ▶ Train the Machine Learning Model

```bash
python train_model.py
```

This generates:

- model.pkl
- accuracy.pkl
- day_encoder.pkl
- season_encoder.pkl

---

## ▶ Run the Flask Application

```bash
python app.py
```

---

## 🌐 Open in Browser

```
http://127.0.0.1:5000
```

or

```
http://localhost:5000
```

---

## 📊 Machine Learning Model

| Property | Value |
|----------|-------|
| Algorithm | Random Forest Regressor |
| Dataset Size | 500 Records |
| Training Data | 80% |
| Testing Data | 20% |
| Features | 7 |
| Target | WaterConsumption |

---

## 📈 Dashboard Features

- Monthly Water Consumption Chart
- Temperature vs Water Consumption
- Rainfall vs Water Consumption
- Water Usage Distribution
- Prediction History
- Model Performance
- Accuracy Progress Bar
- PDF Report Download

---

## 📄 Prediction Report

The application can generate a PDF report containing:

- Input Details
- Prediction Result
- Water Saving Tips

---

## 💡 Water Saving Tips

- Turn off taps while brushing.
- Repair leaking pipes.
- Harvest rainwater.
- Reuse RO wastewater.
- Install water-efficient fixtures.
- Water plants early in the morning.

---

## 🚀 Future Improvements

- User Login System
- Database Integration (MySQL)
- Live Weather API
- Mobile Application
- Email PDF Reports
- Admin Dashboard
- Cloud Deployment
- Real-time Analytics

---

## 👨‍💻 Author

**Avadhut Ramesh Mirage**

Mini Project

Water Consumption Prediction using Machine Learning

---

## 📜 License

This project is created for educational purposes and can be modified or extended for learning and research.