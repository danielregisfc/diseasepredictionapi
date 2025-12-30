from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from app.model.dataset import load_dataset
from app.model.features import FEATURE_NAMES

_model = None


def load_model():
    global _model

    if _model is None:
        df = load_dataset()

        X = df[FEATURE_NAMES]
        y = df["target"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)

        _model = model

    return _model