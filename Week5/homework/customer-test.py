import requests

url = "http://127.0.0.1:9696/predict"
client = {"job": "unknown", "duration": 270, "poutcome": "failure"}

response = requests.post(url, json=client)
response.raise_for_status()
data = response.json()
print(data)