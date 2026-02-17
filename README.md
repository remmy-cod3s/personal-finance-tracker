# Personal Finance Tracker API

A RESTful API for tracking personal expenses with user authentication built with Flask and SQLAlchemy.

## Features

- 🔐 **User Authentication** - Secure registration and login with JWT tokens
- 💰 **Expense Tracking** - Create, view, and delete expenses
- 📊 **Analytics** - Get spending summaries grouped by category
- 🔍 **Filtering** - Filter expenses by category
- 🛡️ **Security** - Password hashing with bcrypt, protected routes

## Tech Stack

- **Backend Framework:** Flask
- **Database:** SQLite with SQLAlchemy ORM
- **Authentication:** JWT (JSON Web Tokens)
- **Password Security:** Bcrypt

## API Endpoints

### Authentication
- `POST /api/register` - Register a new user
- `POST /api/login` - Login and receive JWT token

### Expenses (Protected Routes)
- `POST /api/expenses` - Create a new expense
- `GET /api/expenses` - Get all user expenses
- `GET /api/expenses/category/<category>` - Get expenses by category
- `GET /api/expenses/summary` - Get spending summary by category
- `DELETE /api/expenses/<id>` - Delete an expense

### General
- `GET /` - API status
- `GET /health` - Health check
- `GET /api/profile` - Get user profile (protected)

## Installation

1. Clone the repository
```bash
git clone https://github.com/remmy-cod3s/personal-finance-tracker.git
cd personal-finance-tracker
```

2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000`

## Usage Examples

### Register a User
```bash
POST /api/register
{
  "username": "john",
  "email": "john@example.com",
  "password": "securepassword"
}
```

### Login
```bash
POST /api/login
{
  "username": "john",
  "password": "securepassword"
}
```

### Create Expense (requires token)
```bash
POST /api/expenses
Headers: Authorization: Bearer <your-token>
{
  "amount": 500,
  "category": "food",
  "description": "Lunch at restaurant"
}
```

## Project Structure
```
personal-finance-tracker/
├── app.py              # Main application file
├── models.py           # Database models
├── requirements.txt    # Project dependencies
├── .env               # Environment variables
├── .gitignore         # Git ignore rules
└── finance_tracker.db # SQLite database
```

## Author

**Remonobasi Egbe**
- GitHub: [@remmy-cod3s](https://github.com/remmy-cod3s)
- LinkedIn: [remmy-cod3s](https://linkedin.com/in/remmy-cod3s)

## License

This project is open source and available for educational purposes.
```

