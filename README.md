# ✈️ SkyPrice Estimator

SkyPrice Estimator is a Flask-based machine learning web application that predicts flight prices based on user input features such as airline, route, stops, and travel dates. It provides an engaging multi-step user interface with a flight-ticket styled summary.

---

## 📌 Features

- 🎯 Multi-step interactive booking form
- 📅 Journey and booking date selection
- 🛩️ Select airline, source, destination, and stops
- 📊 Flight price prediction using XGBoost ML model
- 💡 Visually styled result page with ticket summary
- ⚡ Fast predictions with pre-trained model
- 🧠 Encodes user input dynamically before prediction

---

## 🚀 Tech Stack

- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Backend**: Flask
- **ML Model**: XGBoost (with GridSearchCV hyperparameter tuning)
- **Language**: Python 3

---

## 🏗️ Project Structure
```
ML_project/
|
├── templates/ 
│ ├── index.html 
│ └── result.html 
│
├── flight_model.ipynb
├── flight_model.pkl
├── feature_order.json
|
├── Data_Train.xlsx
├── app.py
├── requirements.txt 
└── README.md 
```

---

## 🧪 Example Input & Output

- **Airline**: Air India  
- **Source**: Delhi  
- **Destination**: Cochin  
- **Stops**: 1 Stop  
- **Journey Date**: 2025-07-25  
- **Booking Date**: 2025-07-10  
→ 💰 **Predicted Price**: ₹6,234.75

---

## 🛠️ Installation & Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/skyprice-estimator.git
cd skyprice-estimator
