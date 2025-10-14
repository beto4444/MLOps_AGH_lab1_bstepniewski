from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

def load_data():
    data = load_iris()
    return data.data, data.target, data.target_names


def train_model():
    X, y, _ = load_data()
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    return model


def save_model(model):
    joblib.dump(model, "model.joblib")
