from app.model.train import load_model
from app.model.features import FEATURE_NAMES
import numpy as np


def predict_disease(data):
    model = load_model()

    features = np.array(
        [data[name] for name in FEATURE_NAMES]
    ).reshape(1, -1)

    prediction = model.predict(features)[0]

    return {
        "prediction": bool(prediction)
    }