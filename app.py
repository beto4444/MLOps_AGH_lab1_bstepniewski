from fastapi import FastAPI
from pydantic import BaseModel
from inference import load_model, predict
from training import train_model, save_model


class PredictRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class PredictResponse(BaseModel):
    prediction: str

app = FastAPI()

# Train model and load

model = train_model()
save_model(model)

model = load_model()

@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def app_predict(request: PredictRequest) -> PredictResponse:
    prediction = predict(model, [
        request.sepal_length,
        request.sepal_width,
        request.petal_length,
        request.petal_width
    ])
    encoded_prediction = str(prediction)
    return PredictResponse(prediction=prediction)