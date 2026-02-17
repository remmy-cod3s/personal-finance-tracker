import requests

# First, login to get a token
print("=== Testing Login ===")
login_url = "http://127.0.0.1:5000/api/login"
login_data = {
    "username": "remmy",
    "password": "testpassword123"
}

response = requests.post(login_url, json=login_data)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}\n")

# Get the token
token = response.json()['access_token']
print(f"Token received: {token[:50]}...\n")

# Test 1: Access profile WITH token (should work)
print("=== Test 1: Access profile WITH token ===")
profile_url = "http://127.0.0.1:5000/api/profile"
headers = {
    "Authorization": f"Bearer {token}"
}
response = requests.get(profile_url, headers=headers)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}\n")

# Test 2: Access profile WITHOUT token (should fail)
print("=== Test 2: Access profile WITHOUT token ===")
response = requests.get(profile_url)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}\n")