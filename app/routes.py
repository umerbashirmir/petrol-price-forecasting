from flask import Blueprint, request, jsonify
import pandas as pd
import joblib
import os

main = Blueprint('main', __name__)  # ✅ This is the Blueprint definition

# Load model from ../models/best_model.pkl
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'best_model.pkl')
model = joblib.load(model_path)

@main.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Petrol Price Prediction API is running!"})

@main.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        input_df = pd.DataFrame([{
            'year': data['year'],
            'month': data['month'],
            'day': data['day'],
            'weekday': data['weekday']
        }])

        prediction = model.predict(input_df)[0]
        return jsonify({'predicted_price': round(prediction, 2)})

    except Exception as e:
        return jsonify({'error': str(e)})