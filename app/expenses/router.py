from fastapi import APIRouter, Header, HTTPException
from app.expenses.ai_categorizer import categorize_expense
from app.auth.utils import validate_token
from app.database.crud import get_db
from app.expenses.models import Expense
from sqlalchemy import func
from datetime import datetime

from app.schemas.expenseSchema import ExpenseAdd, TestingExpenseAdd

router = APIRouter()

@router.post("/add")
async def add_expense(payload: ExpenseAdd, token: str = Header(...)):
    db = next(get_db())
    user_id = validate_token(db, token)

    # AI Categorization
    ai_data = await categorize_expense(payload.description)
    expense = Expense(
        user_id=user_id,
        amount=payload.amount,
        description=payload.description,
        category=ai_data.get("category", "Uncategorized"),
        tax_relevant=ai_data.get("tax_relevant", False),
        date=datetime.utcnow()
    )
    db.add(expense)
    db.commit()
    return {"message": "Expense added", 
            "expense": {
            "id": expense.id,
            "amount": expense.amount,
            "description": expense.description,
            "category": expense.category,
            "tax_relevant": expense.tax_relevant,
            "date": expense.date.isoformat(),}
    }

@router.get("/dashboard/summary")
def category_summary(token: str = Header(...)):
    db = next(get_db())
    user_id = validate_token(db, token)
    
    summary = db.query(
        Expense.category,
        func.count(Expense.id).label("count"),
        func.sum(Expense.amount).label("total")
    ).filter(Expense.user_id == user_id).group_by(Expense.category).all()

    # Convert each result row into a dictionary
    summary_list = [
        {
            "category": row[0],
            "count": row[1],
            "total": row[2]
        } for row in summary
    ]
    
    return {"summary": summary_list}

@router.get("/history")
def expense_history(token: str = Header(...)):
    db = next(get_db())
    user_id = validate_token(db, token)
    
    expenses = db.query(Expense).filter(Expense.user_id == user_id).order_by(Expense.date.desc()).all()

    expense_list = []
    for exp in expenses:
        expense_list.append({
            "id": exp.id,
            "amount": exp.amount,
            "description": exp.description,
            "category": exp.category,
            "tax_relevant": exp.tax_relevant,
            "date": exp.date.isoformat()
        })

    return {"expenses": expense_list}


@router.post("/test-categorization")
async def test_categorization(payload: TestingExpenseAdd):
    """Temporary route to test AI categorization"""
    try:
        ai_data = await categorize_expense(payload.description)
        return {
            "description": payload.description,
            "ai_response": ai_data,
            "status": "success"
        }
    except Exception as e:
        return {
            "description": payload.description,
            "error": str(e),
            "status": "error"
        }
