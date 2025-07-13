import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("churn_model.pkl", "rb"))

st.title("Customer Churn Prediction")

# Inputs
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0)

# Example: You’ll later expand inputs to include contract type, internet service, etc.
# Dummy fixed values to match expected model input size
fixed_inputs = np.array([1, 0, 0, 1, 0])  # Example dummies

# Prediction
if st.button("Predict"):
    input_data = np.array([[tenure, monthly_charges, total_charges, *fixed_inputs]])
    prediction = model.predict(input_data)
    result = "Churn" if prediction[0] == 1 else "No Churn"
    st.success(f"Prediction: {result}")
