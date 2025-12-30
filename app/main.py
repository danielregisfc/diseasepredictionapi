from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message":"Api de Predição de Doenças está ativa."

    })

@app.route("/services")
def service():
    return jsonify({
        "status":"ok",
        "service":"disease-prediction-api"
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    required_fields = ["age", "blood_pressure", "cholesterol"]

    if not data:
        return jsonify({"error": "JSON inválido ou vazio"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Campo obrigatório ausente: {field}"}), 400

    return jsonify({
        "message": "Dados válidos recebidos",
        "input": data
    })

if __name__ == "__main__":
    app.run(debug=True)