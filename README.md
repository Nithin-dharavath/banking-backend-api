# Banking Transaction API 🏦

A backend banking transaction management system built using FastAPI and Pydantic.  
This project provides REST APIs for managing bank customers, account details, balances, and transactions.

---

# Features 🚀

- Create new bank customers
- Get all customer details
- Get customer by account ID
- Update customer information
- Delete customer account
- Deposit money
- Withdraw money
- Transaction history management
- Pydantic data validation
- JSON-based data storage
- Swagger API documentation

---

# Tech Stack 🛠️

- Python
- FastAPI
- Pydantic v2
- Uvicorn
- JSON File Storage

---

# Project Structure 📁

```bash
banking_transaction_api/
│
├── main.py
├── data.json
├── requirements.txt
├── README.md
└── venv/
```

---

# Installation ⚙️

## Clone Repository

```bash
git clone <your-github-repo-link>
```

## Navigate to Project

```bash
cd banking_transaction_api
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

# Install Dependencies 📦

```bash
pip install fastapi uvicorn pydantic
```

or

```bash
pip install -r requirements.txt
```

---

# Run Server ▶️

```bash
uvicorn main:app --reload
```

Server runs on:

```bash
http://127.0.0.1:8000
```

---

# API Documentation 📚

Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

ReDoc:

```bash
http://127.0.0.1:8000/redoc
```

---

# API Endpoints 🔥

| Method | Endpoint | Description |
|---|---|---|
| POST | `/create` | Create new customer |
| GET | `/customers` | Get all customers |
| GET | `/customer/{account_id}` | Get customer by ID |
| PUT | `/update/{account_id}` | Update customer |
| DELETE | `/delete/{account_id}` | Delete customer |

---

# Example Customer JSON 🧾

```json
{
  "id": "ACC001",
  "name": "Rahul Sharma",
  "city": "Hyderabad",
  "age": 32,
  "gender": "male",
  "account_type": "savings",
  "balance": 45000.75,
  "currency": "INR",
  "account_status": "active",
  "transactions": [
    {
      "txn_id": "TXN1001",
      "type": "deposit",
      "amount": 10000,
      "status": "success"
    }
  ]
}
```

---

# Validation Features ✅

This project uses Pydantic validation for:

- Required fields
- Data types
- Age constraints
- Transaction validation
- Enum validation using Literal
- Nested transaction schemas

---

# Future Improvements 🚀

- MySQL/PostgreSQL integration
- JWT Authentication
- Password hashing
- Account login system
- Docker deployment
- Frontend integration
- Transfer money API
- Transaction analytics
- Role-based access control

---

# Author 👨‍💻

Nithin

---

# License 📄

This project is for learning and educational purposes.