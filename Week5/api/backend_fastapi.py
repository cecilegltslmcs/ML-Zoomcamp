import pickle
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    '''
    Home page of the application.

    This endpoint is not used by the frontend app.

    Returns:
        str: A greeting message for the user.
    '''
    return 'Welcome to the Churn prediction app'

def load_model():
    '''
    Load the model from a .bin file and create the dictionary vectorizer and the model.

    Returns:
        tuple (dictVectorizer, model): 
            A tuple containing the dictionary vectorizer (dv) and the model (model) trained on data using Scikit-Learn.
    '''
    input_file = '../models/model_C=1.0.bin'
    with open(input_file, 'rb') as f_in: 
        dv, model = pickle.load(f_in)
    return dv, model

@app.post('/predict')
def predict(customer: dict):
    '''
    Predict the likelihood of customer churn and the churn decision based on input customer data.

    Parameters
    ----------
    customer : dict
        A dictionary containing customer information.

        The dictionary must include the following information:
        - customerid (str): Unique identifier for the customer.
        - gender (str): Customer's gender.
        - senior citizen (int): Whether the customer is a senior citizen (0 for No, 1 for Yes).
        - partner (str): Whether the customer has a partner (e.g., 'Yes' or 'No').
        - dependents (str): Whether the customer has dependents (e.g., 'Yes' or 'No').
        - tenure (int): Number of months the customer has been with the company.
        - phoneservice (str): Whether the customer has phone service (e.g., 'Yes' or 'No').
        - multiplelines (str): Whether the customer has multiple phone lines (e.g., 'Yes,' 'No,' or 'No phone service').
        - internetservice (str): Type of internet service (e.g., 'DSL,' 'Fiber optic,' or 'No').
        - onlinesecurity (str): Whether the customer has online security (e.g., 'Yes,' 'No,' or 'No internet service').
        - onlinebackup (str): Whether the customer has online backup (e.g., 'Yes,' 'No,' or 'No internet service').
        - deviceprotection (str): Whether the customer has device protection (e.g., 'Yes,' 'No,' or 'No internet service').
        - techsupport (str): Whether the customer has tech support (e.g., 'Yes,' 'No,' or 'No internet service').
        - streamingtv (str): Whether the customer has streaming TV (e.g., 'Yes,' 'No,' or 'No internet service').
        - streamingmovies (str): Whether the customer has streaming movies (e.g., 'Yes,' 'No,' or 'No internet service').
        - contract (str): Type of contract (e.g., 'Month-to-month,' 'One year,' 'Two year').
        - paperlessbilling (str): Whether the customer receives paperless billing (e.g., 'Yes' or 'No').
        - paymentmethods (str): Payment method used by the customer.
        - monthlycharges (float): Monthly charges for the service.
        - totalcharges (float): Total charges incurred by the customer.

    Returns
    -------
    dict
        A dictionary containing the results of the prediction.

        Keys:
        - 'churn_probability' (float): The probability of churn.
        - 'churn_decision' (bool): The churn decision (True for churn, False for no churn).
        
    Example Request Body:
    ```json
    {
        'customerid': '8879-zkjof',
        'gender': 'female',
        'seniorcitizen': 0,
        'partner': 'no',
        'dependents': 'no',
        'tenure': 2,
        'phoneservice': 'yes',
        'multiplelines': 'no',
        'internetservice': 'dsl',
        'onlinesecurity': 'yes',
        'onlinebackup': 'yes',
        'deviceprotection': 'yes',
        'techsupport': 'yes',
        'streamingtv': 'yes',
        'streamingmovies': 'yes',
        'contract': 'one_year',
        'paperlessbilling': 'no',
        'paymentmethod': 'bank_transfer_(automatic)',
        'monthlycharges': 79.85,
        'totalcharges': 3320.75   
    }
    ```
    
    Example Response: 
    ```json
    {
        'churn_probability': 0.122,
        'churn_decision': False
    }
    ```
    
    '''
    dv, model = load_model()
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5
    result = {
        'churn_probability': float(y_pred),
        'churn' : bool(churn)
    }
    return result