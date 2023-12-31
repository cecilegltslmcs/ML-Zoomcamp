import requests
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("url_eba")
url = f'http://127.0.0.1:8000/predict'

customer = {
  "customerid": "8879-zkjof",
  "gender": "female",
  "seniorcitizen": 0,
  "partner": "no",
  "dependents": "no",
  "tenure": 2,
  "phoneservice": "yes",
  "multiplelines": "no",
  "internetservice": "dsl",
  "onlinesecurity": "yes",
  "onlinebackup": "yes",
  "deviceprotection": "yes",
  "techsupport": "yes",
  "streamingtv": "yes",
  "streamingmovies": "yes",
  "contract": "one_year",
  "paperlessbilling": "no",
  "paymentmethod": "bank_transfer_(automatic)",
  "monthlycharges": 79.85,
  "totalcharges": 3320.75
}
response = requests.post(url, json=customer)
response.raise_for_status()
data = response.json()
print(data)

if data['churn'] == True:
    print(f"sending promo email to {customer['customerid']}")
else:
  print(f"Not sending promo email to {customer['customerid']}")
