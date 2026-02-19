import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="Heart Disease Predictor")

st.title("❤️ Heart Disease Prediction System")
st.write("Enter patient details below to predict heart disease.")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=30)
    sex = st.selectbox("Sex", ["Female", "Male"])
    chest_pain_type = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3)
    resting_bp = st.number_input("Resting Blood Pressure", value=120)
    cholesterol = st.number_input("Cholesterol", value=200)
    fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])

with col2:
    resting_ecg = st.number_input("Resting ECG (0-2)", min_value=0, max_value=2)
    max_heart_rate = st.number_input("Max Heart Rate", value=150)
    exercise_angina = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
    st_depression = st.number_input("ST Depression", value=1.0)
    st_slope = st.number_input("ST Slope (0-2)", min_value=0, max_value=2)
    num_major_vessels = st.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3)
    thalassemia = st.number_input("Thalassemia (0-3)", min_value=0, max_value=3)

# Convert categorical values
sex = 1 if sex == "Male" else 0
fasting_blood_sugar = 1 if fasting_blood_sugar == "Yes" else 0
exercise_angina = 1 if exercise_angina == "Yes" else 0

st.markdown("")

if st.button("Predict"):

    data = {
        "age": age,
        "sex": sex,
        "chest_pain_type": chest_pain_type,
        "resting_bp": resting_bp,
        "cholesterol": cholesterol,
        "fasting_blood_sugar": fasting_blood_sugar,
        "resting_ecg": resting_ecg,
        "max_heart_rate": max_heart_rate,
        "exercise_angina": exercise_angina,
        "st_depression": st_depression,
        "st_slope": st_slope,
        "num_major_vessels": num_major_vessels,
        "thalassemia": thalassemia
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        result = response.json()

        if result["prediction"] == 1:
            st.error("❌ Heart Disease Detected")
        else:
            st.success("✅ No Heart Disease")

    except:
        st.warning("⚠ Backend not running. Please start FastAPI server.")
