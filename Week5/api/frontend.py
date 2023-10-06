import streamlit as st
import requests
import json

st.title("Churn Prediction Application")
c1, c2 = st.columns(2)


with c1.form("Enter the informations for your customer"):
    customer_id = st.text_input("Customer Id")
    gender = st.radio("Select gender:", ["Female", "Male"])
    senior_citizen = st.number_input("Senior Citizen")
    partner = st.radio("Has a partner:", ["Yes", "No"])
    dependents = st.radio("Has dependents:", ["Yes", "No"])
    tenure = st.number_input("Tenure")
    phone_service = st.radio("Has phone service:", ["Yes", "No"])
    multiple_lines = st.radio("Has multiple lines:", ["Yes", "No"])
    internet_services = st.radio("Has Internet Service:", ["DSL", "Fiber optic", "No"])
    online_security = st.radio("Has Online Security:", ["Yes", "No"])
    online_backup = st.radio("Has Online Backup:", ["Yes", "No"])
    device_protection = st.radio("Has device protection:",["Yes", "No"])
    tech_support = st.radio("Has tech Support:", ["Yes", "No"])
    streaming_TV = st.radio("Has Streaming TV:", ["Yes", "No"])
    streaming_movies = st.radio("Has Streaming Movies:", ["Yes", "No"])
    contract = st.radio("Which types of contract:", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.radio("Paperless Billing:", ["Yes", "No"])
    payment_method = st.radio("Which payment method: ", ["Electronic check", "Mailed check", "Bank transfer (automatic)"," Credit card (automatic)"])
    monthly_charges = st.number_input("Monthly Charges")
    total_charges = st.number_input("Total Charges")
    
    submitted = st.form_submit_button("Submit")

contract = contract.replace(" ", "_").lower()
payment_method = payment_method.replace(" ", "_").lower()

customer = {
    "customerid": customer_id,
    "gender": gender.lower(),
    "seniorcitizen": senior_citizen,
    "partner": partner.lower(),
    "dependents": dependents.lower(),
    "tenure": tenure,
    "phoneservice": phone_service.lower(),
    "multiplelines": multiple_lines.lower(),
    "internetservice": internet_services.lower(),
    "onlinesecurity": online_security.lower(),
    "onlinebackup": online_backup.lower(),
    "deviceprotection": device_protection.lower(),
    "techsupport": tech_support.lower(),
    "streamingtv": streaming_TV.lower(),
    "streamingmovies": streaming_movies.lower(),
    "contract": contract.lower(),
    "paperlessbilling": paperless_billing.lower(),
    "paymentmethod": payment_method,
    "monthlycharges": monthly_charges,
    "totalcharges": float(total_charges)
}

if submitted:
    json_customer = json.dumps(customer, indent=4)
    headers = {"Content-Type": "application/json"}
    req = requests.post("http://127.0.0.1:8000/predict",
                        data=json_customer,
                        headers = headers)
    result = req.json()

    if result['churn'] == True:
        c2.subheader(f"Customer :red[{customer['customerid']}] will churn. Send an email!")
    else:
        c2.subheader(f"Customer :green[{customer['customerid']}] will not churn.")