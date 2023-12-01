import requests
# url = 'http://localhost:9696'

url = "http://localhost:8080"

data = {'url': 'http://bit.ly/mlbookcamp-pants'}

result = requests.post(url, json=data).json()
print(result)
