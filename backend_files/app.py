import sys
import os
import logging
import joblib
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.pipeline import Pipeline

# Ensure backend_files directory is in sys.path so modules can find custom_transformers
backend_dir = os.path.abspath('backend_files')
if backend_dir not in sys.path:
    sys.path.append(backend_dir)

# Import the custom transformer functions
import custom_transformers
from custom_transformers import (
    calculate_store_age_func,
    extract_product_id_char_func,
    standardize_sugar_content,
    classify_product_type_category
)

# Securely register custom functions on __main__ for joblib unpickling compatibility
for _name in [
    'calculate_store_age_func',
    'extract_product_id_char_func',
    'standardize_sugar_content',
    'classify_product_type_category'
]:
    setattr(sys.modules['__main__'], _name, getattr(custom_transformers, _name))

# Suppress internal colab debug/repr evaluation logs
logging.getLogger('werkzeug').setLevel(logging.ERROR)

app = Flask(__name__)
MODEL_PATH = 'backend_files/superkart_model.joblib'

def load_model(path):
    try:
        model = joblib.load(path)
        if isinstance(model, Pipeline):
            return model
        else:
            raise TypeError("Loaded object is not a scikit-learn Pipeline.")
    except FileNotFoundError:
        print(f"Error: Model file not found at {path}")
        return None
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

model_pipeline = load_model(MODEL_PATH)

@app.route('/')
def home():
    return "SuperKart Sales Prediction API. Use /v1/predict for single predictions or /v1/predictbatch for batch predictions."

@app.route('/v1/predict', methods=['POST'])
def predict():
    if model_pipeline is None:
        return jsonify({'error': 'Model not loaded'}), 500
    try:
        json_data = request.get_json()
        if not json_data:
            return jsonify({'error': 'No JSON data provided'}), 400
        input_df = pd.DataFrame([json_data])
        prediction = model_pipeline.predict(input_df)[0]
        return jsonify({'predicted_sales': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/v1/predictbatch', methods=['POST'])
def predict_batch():
    if model_pipeline is None:
        return jsonify({'error': 'Model not loaded'}), 500
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file and file.filename.endswith('.csv'):
            input_df = pd.read_csv(file)
            predictions = model_pipeline.predict(input_df)
            return jsonify({'predictions': predictions.tolist()})
        else:
            return jsonify({'error': 'Invalid file type. Please upload a CSV file.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
