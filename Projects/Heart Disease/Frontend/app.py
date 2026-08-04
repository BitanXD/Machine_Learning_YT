import streamlit as st
import pandas as pd
import joblib

model = joblib.load('E:/Machine Learning/Projects/Heart Disease/Pickle Files/KNN_heart.pkl')
scaler = joblib.load('E:/Machine Learning/Projects/Heart Disease/Pickle Files/scaler.pkl')
expected_columns = joblib.load('E:/Machine Learning/Projects/Heart Disease/Pickle Files/columns.pkl')

st.title("Heart Disease Prediction using KNN")
st.markdown("Provide the following details:")

age = st.slider("Age",18,100,40)
sex = st.selectbox("Sex",['M','F'])
chest_pain = st.selectbox("Chest Pain Type", ["ATA","NAP","TA","ASY"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)",80,200,120)
cholestrol = st.number_input("Cholestrol (mm/dL)",100,600,200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mm/dL", [0,1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_HR = st.slider("Max Heart Rate", 60,220,150)
exercise_angina = st.selectbox("Exercise Induced Angina", ["Y","N"])
old_peak = st.slider("Old Peak (ST depression)",0.0,6.0,1.0)
st_slope = st.selectbox("ST Slope", ["Up","Flat","Down"])

if st.button("Predict"):
    raw_input = {
        'Age': age,
        'RestingBP' : resting_bp,
        'Cholesterol' : cholestrol,
        'FastingBS' : fasting_bs,
        'MaxHR' : max_HR,
        'Oldpeak' : old_peak,
        'Sex_' + sex : 1,
        'ChestPainType_' + chest_pain : 1,
        'RestingECG_' + resting_ecg : 1,
        'ExerciseAngina_' + exercise_angina : 1,
        'ST_Slope_' + st_slope : 1
    }

    input_df = pd.DataFrame([raw_input])
    
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    numeric_cols = list(scaler.feature_names_in_)
    input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

    prediction = model.predict(input_df)[0]

    if prediction == 0:
        st.markdown("No Heart Disease detected :white_check_mark:")
    else:
        st.markdown("Heart Disease detected :red_cross:")