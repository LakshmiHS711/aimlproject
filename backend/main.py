from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

app = FastAPI()

# Load trained model
with open("heart_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define request body
class HeartData(BaseModel):
    age: int
    sex: int
    chest_pain_type: int
    resting_bp: float
    cholesterol: float
    fasting_blood_sugar: int
    resting_ecg: int
    max_heart_rate: float
    exercise_angina: int
    st_depression: float
    st_slope: int
    num_major_vessels: int
    thalassemia: int

@app.get("/")
def home():
    return {"message": "Heart Disease Prediction API"}

@app.post("/predict")
def predict(data: HeartData):
    input_data = np.array([[
        data.age,
        data.sex,
        data.chest_pain_type,
        data.resting_bp,
        data.cholesterol,
        data.fasting_blood_sugar,
        data.resting_ecg,
        data.max_heart_rate,
        data.exercise_angina,
        data.st_depression,
        data.st_slope,
        data.num_major_vessels,
        data.thalassemia
    ]])

    prediction = model.predict(input_data)[0]

    return {
        "prediction": int(prediction),
        "result": "Heart Disease Detected" if prediction == 1 else "No Heart Disease"
    }
