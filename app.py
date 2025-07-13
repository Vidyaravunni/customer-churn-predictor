import streamlit as st
import pickle
import numpy as np

st.title("Customer Churn Predictor")

# Sample Inputs
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges")
total_charges = st.number_input("Total Charges")

# Dummy: Replace this with actual encoding logic
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

if st.button("Predict"):
    # Dummy feature vector
    input_data = np.array([[tenure, monthly_charges, total_charges, 1, 0, 0]])
    model = pickle.load(open("churn_model.pkl", "rb"))
    prediction = model.predict(input_data)

    st.write("Churn Prediction:", "Yes" if prediction[0]==1 else "No")
