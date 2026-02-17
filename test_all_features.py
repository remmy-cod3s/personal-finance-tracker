import requests

# Login
login_url = "http://127.0.0.1:5000/api/login"
response = requests.post(login_url, json={"username": "remmy", "password": "testpassword123"})
token = response.json()['access_token']
headers = {"Authorization": f"Bearer {token}"}

print("=== Testing Expense Features ===\n")

# 1. Get all expenses
print("1. Getting all expenses:")
response = requests.get("http://127.0.0.1:5000/api/expenses", headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}\n")

# 2. Get expenses by category (food)
print("2. Getting food expenses:")
response = requests.get("http://127.0.0.1:5000/api/expenses/category/food", headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}\n")

# 3. Get spending summary
print("3. Getting spending summary:")
response = requests.get("http://127.0.0.1:5000/api/expenses/summary", headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}\n")

# 4. Delete an expense (expense with id=1)
print("4. Deleting expense ID 1:")
response = requests.delete("http://127.0.0.1:5000/api/expenses/1", headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}\n")

# 5. Get all expenses again (should only have 1 now)
print("5. Getting all expenses after deletion:")
response = requests.get("http://127.0.0.1:5000/api/expenses", headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}\n")