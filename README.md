# Petrol Price Forecasting API

This is a Flask-based machine learning API that predicts petrol prices based on date inputs (year, month, day, weekday). It uses a trained LightGBM model and is deployed on Render.

---

## Live Demo

 Try it now:  https://petrol-price-forecasting-api.onrender.com

---

##  API Endpoints

### `GET /`
Returns API status.

**Response:**
```json
{
  "message": "Petrol Price Prediction API is running!"
}

POST /predict
Predict petrol price based on date input.

Request JSON:
{
  "year": 2025,
  "month": 6,
  "day": 10,
  "weekday": 0
}
RESPONSE :
{
  "predicted_price": 75.23
}

Model Details
Trained using LightGBM on historical petrol price data

Features used: year, month, day, weekday

Model file: best_model.pkl


Tech Stack
Python

Flask

LightGBM

Pandas

Render (Deployment)



PROJECT STRUCTURE
petrol-price-forecasting/
├── app/
│   ├── __init__.py
│   └── routes.py
├── models/
│   └── best_model.pkl
├── main.py
├── requirements.txt
└── README.md


HOW TO RUN LOCALLY
git clone   :  https://github.com/Abbasnazir/petrol-price-forecasting-api.git
cd petrol-price-forecasting-api
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python main.py




Author
Abaas Nazir
BA Economics, IGNOU
Data Science Enthusiast | Python | ML | Flask
 Kupwara, India

 Contact
Email: abbasnazir912@gmail.com
