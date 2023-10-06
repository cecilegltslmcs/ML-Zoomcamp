import pickle
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Welcome to the Churn prediction app"

def load_model():
    input_file = "../models/model_C=1.0.bin"
    with open(input_file, 'rb') as f_in: 
        dv, model = pickle.load(f_in)
    return dv, model

@app.post("/predict")
def predict(customer: dict):
    dv, model = load_model()
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5
    result = {
        'churn_probability': float(y_pred),
        'churn' : bool(churn)
    }
    return result