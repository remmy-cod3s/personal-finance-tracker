import requests

# First, login to get token
login_url = "http://127.0.0.1:5000/api/login"
login_data = {
    "username": "remmy",
    "password": "testpassword123"
}

response = requests.post(login_url, json=login_data)
token = response.json()['access_token']
headers = {"Authorization": f"Bearer {token}"}

print("=== Creating Expenses ===\n")

# Create expense 1
expense_url = "http://127.0.0.1:5000/api/expenses"
expense1 = {
    "amount": 500,
    "category": "food",
    "description": "Lunch at Chicken Republic"
}

response = requests.post(expense_url, json=expense1, headers=headers)
print(f"Expense 1: {response.status_code}")
print(f"Response: {response.json()}\n")

# Create expense 2
expense2 = {
    "amount": 1500,
    "category": "transport",
    "description": "Uber to campus"
}

response = requests.post(expense_url, json=expense2, headers=headers)
print(f"Expense 2: {response.status_code}")
print(f"Response: {response.json()}\n")

# Get all expenses
print("=== Getting All Expenses ===\n")
response = requests.get(expense_url, headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")