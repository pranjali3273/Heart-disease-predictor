import streamlit as st
import numpy as np
import pickle

# Load the model
model = pickle.load(open('heart_disease_model.pkl', 'rb'))

st.title("💓 Heart Disease Prediction App")

st.markdown("Provide the following health data to predict the risk of heart disease:")

# User inputs
age = st.number_input("Age", min_value=1, max_value=120)
sex = st.selectbox("Sex", ["Female", "Male"])
cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Serum Cholesterol (mg/dl)")
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved")
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("ST Depression", format="%.2f")
slope = st.selectbox("Slope of ST segment", [0, 1, 2])
ca = st.selectbox("Major Vessels Colored (0–3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (1 = normal, 2 = fixed, 3 = reversible)", [1, 2, 3])

# Predict button
if st.button("Predict"):
    sex_val = 1 if sex == "Male" else 0
    input_data = np.array([[age, sex_val, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ The person is likely to have heart disease.")
    else:
        st.success("✅ The person is not likely to have heart disease.")
