# app.py
import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("loan.pkl", "rb"))

st.set_page_config(page_title="Loan Prediction App", layout="centered")
st.title("🏦 Loan Approval Prediction")

st.markdown("Enter the applicant's information:")

# User inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
loan_amount_term = st.selectbox("Loan Amount Term", [360, 180, 120, 240, 300])
credit_history = st.selectbox("Credit History", ["Has Credit History", "No Credit History"])
property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

# Encoding like training
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
dependents = 3 if dependents == "3+" else int(dependents)
education = 0 if education == "Graduate" else 1
self_employed = 1 if self_employed == "Yes" else 0
credit_history = 1 if credit_history == "Has Credit History" else 0
property_area = {"Urban": 2, "Rural": 0, "Semiurban": 1}[property_area]

# Prediction
if st.button("Predict"):
    input_data = np.array([[gender, married, dependents, education, self_employed,
                            applicant_income, coapplicant_income, loan_amount,
                            loan_amount_term, credit_history, property_area]])

    prediction = model.predict(input_data)

    result = "Approved ✅" if prediction[0] == 1 else "Rejected ❌"
    st.success(f"Loan Status: {result}")
# done 