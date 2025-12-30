from flask import Flask, jsonify

app = Flask(__name__)
app.json.ensure_ascii = False


@app.route("/")
def home():
    return jsonify({
        "message": "API de predição está ativa"
    })

@app.route("/status")
def status():
    return jsonify({
        "status": "ok",
        "service": "disease-prediction-api"
    })

if __name__ == "__main__":
    app.run(debug=True)