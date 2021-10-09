import requests

url = "http://0.0.0.0:9696/predict"
customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}
response = requests.post(url, json=customer).json()
print(response)