# High-Level Design (HLD): Petrol Price Forecasting API
PURPOSE :  it shows the big picture how components work together  , key tech stack  , and overall flow.


##  Objective

Create a machine learning API that predicts petrol prices based on a given date using a trained LightGBM model, served via Flask and deployed on Render.



##  Architecture Overview


## ⚙ Components

| Component       | Description                           |
|----------------|---------------------------------------|
| main.py       | App entry point (starts Flask server) |
| app/__init__.py | Initializes and registers API routes |
| app/routes.py  | Handles /predict and root routes   |
| models/best_model.pkl | Trained LightGBM model file   |
| requirements.txt | All dependencies for deployment   |

---

##  Deployment Flow

1. Code is pushed to GitHub
2. Render auto-builds from repo
3. Flask runs with python main.py
4. Model is loaded → Prediction route works live

---

##  API Endpoint Summary

- GET / – Status check  
- POST /predict – Get predicted petrol price

---

## Tech Stack

- Python, Flask, LightGBM, Pandas
- Deployment: Render
- API Testing: Postman, Thunder Client
















