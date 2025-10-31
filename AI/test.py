import requests

data = {"query": "I love movies like Inception"}
response = requests.post("http://127.0.0.1:8000/recommend", json=data)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
