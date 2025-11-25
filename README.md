# ChillTax

**Smart Expense Tracking with Built-in Tax Optimization**

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Sonar AI](https://img.shields.io/badge/Sonar_AI-FF6C37?style=for-the-badge&logo=openai&logoColor=white)

<img width="600" height="150" alt="ChillTax Banner" src="https://github.com/user-attachments/assets/2da13ec2-9b9a-407e-bb73-4fde1a1691ed" />

---

## 🚀 Important Links

### 🎥 Demo Video

<a href="https://vimeo.com/1140351506">
  <img src="./chilltaxthumbnail.png" alt="ChillTax Demo" width="600"/>
</a>

### 🔹 **Hackathon Page and Team Info**  
👉 https://devpost.com/software/xx-6iq0mz

---

## What ChillTax Does

Tax season is stressful. Sorting through receipts, categorizing expenses, and figuring out what's deductible takes hours. ChillTax handles all of that automatically.

Instead of manually tagging every transaction, you just add your expenses with a quick description. Our AI figures out whether it's tax-deductible and sorts it into the right category. When tax time comes, you get a ready-to-file report in seconds.

We also suggest donation opportunities that maximize your tax benefits, because giving back shouldn't mean doing extra paperwork.

---

## System Workflow

```mermaid
graph TB
    A[User Adds Expense] --> B[Perplexity AI Analysis]
    B --> C{Tax Deductible?}
    C -->|Yes| D[Categorize as Work/Medical/etc]
    C -->|No| E[Mark as Personal]
    D --> F[Store in PostgreSQL]
    E --> F
    F --> G[Dashboard Updates]
    G --> H[Generate Reports]
    H --> I[Export PDF/CSV]
    
    style A fill:#e3f2fd,stroke:#1e88e5,color:#01579b
    style B fill:#fff3e0,stroke:#f57c00,color:#e65100
    style C fill:#fce4ec,stroke:#c2185b,color:#880e4f
    style D fill:#e8f5e9,stroke:#43a047,color:#1b5e20
    style E fill:#ffebee,stroke:#e53935,color:#b71c1c
    style F fill:#f3e5f5,stroke:#8e24aa,color:#4a148c
    style G fill:#e1f5fe,stroke:#0288d1,color:#01579b
    style H fill:#fff8e1,stroke:#fdd835,color:#f57f17
    style I fill:#e8f5e9,stroke:#43a047,color:#1b5e20
```

**How it works:**
1. User enters expense amount and description
2. Perplexity AI analyzes the context and determines tax relevance
3. System categorizes and stores the transaction
4. Dashboard displays real-time spending patterns
5. One-click export generates tax-ready documents

---

## Core Features

**Intelligent Categorization**  
Describe your expense naturally, and the AI decides if it's deductible and what category it belongs to. No dropdown menus or manual tagging required.

**Real-Time Dashboard**  
See exactly where your money goes, broken down by category. Track tax-deductible vs personal spending at a glance.

**Tax-Ready Exports**  
Generate PDFs for your accountant or CSV files compatible with German tax software like ELSTER and WISO. Everything formatted correctly, nothing to edit.

**Donation Recommendations**  
Get suggestions for NGOs where your contributions qualify for tax deductions. Know exactly how much you'll save before you donate.

**Secure Authentication**  
Token-based auth keeps your financial data protected. Each user's expenses are completely isolated.

---

## API Reference

### Authentication Endpoints

**Create Account**  
`POST /auth/signup`

```json
{
  "name": "Rahul",
  "email": "rahul@tax.com",
  "username": "tax_rahul",
  "password": "securepassword123",
  "phone": "9876543210"
}
```

Returns authentication token and user ID.

**Login**  
`POST /auth/login`

```json
{
  "email_or_username": "tax_rahul",
  "password": "securepassword123"
}
```

Returns authentication token for subsequent requests.

---

### Expense Management

**Add New Expense**  
`POST /expenses/add`

Requires `Authorization: Bearer <token>` header.

```json
{
  "amount": 5000,
  "description": "MacBook Pro for coding"
}
```

The AI automatically categorizes this as "Work" and marks it tax-deductible.

**Dashboard Summary**  
`GET /expenses/dashboard`

Returns category-wise breakdown with totals and tax relevance.

**Complete History**  
`GET /expenses/history`

Chronological list of all expenses with full details.

---

### Export Options

**PDF Report**  
`GET /exports/pdf`

Downloads a formatted tax report ready for filing.

**CSV Export**  
`GET /exports/csv`

Generates spreadsheet-compatible file with columns: ID, Amount, Category, Description, Date, Tax_Relevant.

---

### Tax Optimization

**Donation Suggestions**  
`GET /donations/suggestions`

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

---

## Setup Guide

**Requirements**
- Python 3.10 or higher
- PostgreSQL database
- Perplexity API key

**Installation Steps**

Clone the repository:
```bash
git clone https://github.com/manojkp08/ChillTax_Perplexity_Devpost.git
cd ChillTax_Perplexity_Devpost
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Configure environment variables in `.env`:
```ini
DATABASE_URL=postgresql://user:password@localhost:5432/taxfighter
PERPLEXITY_API_KEY=your_key_here
```

Start the server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

---

## Technical Architecture

**Backend Framework:** FastAPI handles routing and request validation  
**Database:** PostgreSQL stores user data and transactions  
**AI Engine:** Perplexity Sonar API powers expense categorization  
**Cloud Infrastructure:** Google Cloud Platform hosts production deployment  
**Security:** Token-based authentication with secure password hashing  
**Export Libraries:** FPDF2 for PDFs, native CSV module for spreadsheets

---

## Live Deployment

Production API: `https://chilltax-perplexity-devpost.onrender.com`

All endpoints documented above work on this base URL. Include your auth token in the headers for protected routes.

---

## Error Handling

The API returns standard HTTP status codes:
- **200:** Request successful
- **201:** Resource created
- **400:** Invalid request data
- **401:** Authentication required or invalid token
- **404:** Resource not found
- **500:** Server error

Error responses include a `detail` field explaining what went wrong.
