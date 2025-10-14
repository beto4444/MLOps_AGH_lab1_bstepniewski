import joblib
from training import load_data
def load_model():
    return joblib.load("model.joblib")

def predict(model, features):
    _, _, target_names = load_data()
    prediction = model.predict([features])[0]
    return target_names[prediction]