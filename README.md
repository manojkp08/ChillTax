# 📌 ChillTax
**AI-Powered Expense Tracker for Tax Optimization**

<div align="center">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Sonar_AI-FF6C37?style=for-the-badge&logo=openai&logoColor=white" />
</div>

<img width="800" height="190" alt="image" src="https://github.com/user-attachments/assets/2da13ec2-9b9a-407e-bb73-4fde1a1691ed" />


## 🚀 Important Links

### 🎥 Demo Video

<a href="https://vimeo.com/1140351506">
  <img src="./chilltaxthumbnail.png" alt="ChillTax Demo" width="600"/>
</a>

### 🔹 **Hackathon Page and Team Info**  
👉 https://devpost.com/software/xx-6iq0mz

## 🚀 Features

- **AI-Powered Expense Categorization** (Tax vs. Non-Tax)
- **Real-Time Dashboard** with Spending Insights
- **PDF/CSV Export** for Tax Filing
- **Donation Suggestions** with Tax Benefits
- **User Authentication**

## 📡 API Endpoints

### 🔐 Authentication

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/auth/signup` | POST | Create account (Name, Email, Password) |
| `/auth/login` | POST | Login (Email/Username + Password) |

### 💸 Expenses

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/expenses/add` | POST | Add expense (Auto-categorized by AI) |
| `/expenses/dashboard/summary` | GET | Category-wise spending summary |
| `/expenses/history` | GET | Full expense history (Chronological) |

### 📤 Exports

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/exports/pdf` | GET | Generate PDF tax report |
| `/exports/csv` | GET | Generate CSV for ELSTER/WISO |

### ❤️ Donations

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/donations/suggestions` | GET | Tax-beneficial NGO recommendations |

## 🛠️ Setup

### Prerequisites

- Python 3.10+
- PostgreSQL
- Perplexity API Key

### Installation

```bash
git clone https://github.com/manojkp08/ChillTax_Perplexity_Devpost.git  
cd ChillTax_Perplexity_Devpost  
pip install -r requirements.txt  
```

### Environment Variables

Create `.env` file:

```ini
DATABASE_URL=postgresql://user:password@localhost:5432/taxfighter  
PERPLEXITY_API_KEY=your_key_here    
```

### Run Locally

```bash
uvicorn app.main:app --reload  
```

## 📄 Example API Requests

### 1️⃣ AUTHENTICATION

#### Signup
**POST** `https://chilltax-perplexity-devpost.onrender.com/auth/signup`

**Request Body:**
```json
{
  "name": "Rahul",
  "email": "rahul@tax.com",
  "username": "tax_rahul",
  "password": "securepassword123",
  "phone": "9876543210"
}
```

**Success Response (201):**
```json
{
  "token": "a1b2c3d4e5",
  "user_id": 1
}
```

**Error (400):**
```json
{
  "detail": "Email already registered"
}
```

#### Login
**POST** `https://chilltax-perplexity-devpost.onrender.com/auth/login`

**Request Body:**
```json
{
  "email_or_username": "tax_rahul",
  "password": "securepassword123"
}
```

**Success Response (200):**
```json
{
  "token": "a1b2c3d4e5"
}
```

**Error (401):**
```json
{
  "detail": "Invalid credentials"
}
```

### 2️⃣ EXPENSES

#### Add Expense (AI-Powered)
**POST** `https://chilltax-perplexity-devpost.onrender.com/expenses/add`

**Headers:**
```
Authorization: Bearer a1b2c3d4e5
```

**Request Body:**
```json
{
  "amount": 5000,
  "description": "MacBook Pro for coding"
}
```

**Success Response (200):**
```json
{
  "category": "Work",
  "tax_relevant": true,
  "message": "Expense added"
}
```

**Error (401):**
```json
{
  "detail": "Invalid token"
}
```

#### Get Dashboard Summary
**GET** `https://chilltax-perplexity-devpost.onrender.com/expenses/dashboard`

**Headers:**
```
Authorization: Bearer a1b2c3d4e5
```

**Success Response (200):**
```json
{
  "summary": [
    {
      "category": "Work",
      "count": 5,
      "total_amount": 25000,
      "tax_relevant": true
    }
  ]
}
```

#### Full Expense History
**GET** `https://chilltax-perplexity-devpost.onrender.com/expenses/history`

**Success Response (200):**
```json
{
  "expenses": [
    {
      "id": 1,
      "amount": 5000,
      "category": "Work",
      "description": "MacBook Pro",
      "date": "2023-10-20T12:00:00"
    }
  ]
}
```

### 3️⃣ EXPORTS

#### PDF Export
**GET** `https://chilltax-perplexity-devpost.onrender.com/exports/pdf`

**Headers:**
```
token: a1b2c3d4e5
```

**Response:**
- Direct PDF download (`tax_report.pdf`)

#### CSV Export
**GET** `/exports/csv`

**Response:**
- CSV file (`tax_report.csv`) with columns:
- ID,Amount,Category,Description,Date,Tax_Relevant

### 4️⃣ DONATIONS

#### Tax-Beneficial Suggestions
**GET** `https://chilltax-perplexity-devpost.onrender.com/donations/suggestions`

**Success Response (200):**
```json
{
  "suggestions": [
    {
      "ngo": "Teach For India",
      "cause": "Education",
      "tax_benefit": "50% under 80G",
      "min_amount": 500
    }
  ]
}
```

## 💡 Tech Stack

- **Backend:** FastAPI
- **Database:** PostgreSQL
- **Cloud Platform:** Google Cloud Platform
- **AI:** Perplexity Sonar API
- **Auth:** Tokens Based
- **Export:** PDF (FPDF2), CSV
