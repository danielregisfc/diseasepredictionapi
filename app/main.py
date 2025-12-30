from flask import Flask, jsonify

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

if __name__ == "__main__":
    app.run(debug=True)