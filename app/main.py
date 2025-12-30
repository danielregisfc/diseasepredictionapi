from flask import Flask, jsonify
from app.config import Config
from app.routes.predict import predict_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(predict_bp)

    @app.route("/")
    def index():
        return jsonify({"message": "API de predição está ativa"})

    @app.route("/status")
    def status():
        return jsonify({"status": "ok"})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()