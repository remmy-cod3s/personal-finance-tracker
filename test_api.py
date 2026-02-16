import requests

# Test registration
url = "http://127.0.0.1:5000/api/register"
data = {
    "username": "remmy",
    "email": "remon@gmail.com",
    "password": "testpassword123"
}

response = requests.post(url, json=data)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")


