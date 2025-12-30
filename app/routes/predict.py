from flask import Blueprint, request, jsonify
from app.services.prediction_service import predict_disease

predict_bp = Blueprint("predict", __name__)


@predict_bp.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON inválido ou vazio"}), 400

    try:
        result = predict_disease(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500