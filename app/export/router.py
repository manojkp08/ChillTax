from fastapi import APIRouter, Header
from fastapi.responses import FileResponse
from app.expenses.models import Expense
from app.auth.utils import validate_token
from app.database.crud import get_db
from app.export.pdf_generator import create_pdf
import csv
import os

router = APIRouter()

@router.get("/pdf")
async def export_pdf(token: str = Header(...)):
    db = next(get_db())
    user_id = validate_token(db, token)
    expenses = db.query(Expense).filter(Expense.user_id == user_id).all()
    
    # Generate PDF
    pdf_path = create_pdf(expenses)
    return FileResponse(pdf_path, filename="tax_report.pdf")

@router.get("/csv")
async def export_csv(token: str = Header(...)):
    db = next(get_db())
    user_id = validate_token(db, token)
    expenses = db.query(Expense).filter(Expense.user_id == user_id).all()
    
    # Generate CSV
    csv_path = "tax_report.csv"
    with open(csv_path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Amount", "Category", "Description", "Date"])
        for exp in expenses:
            writer.writerow([exp.id, exp.amount, exp.category, exp.description, exp.date])
    
    return FileResponse(csv_path, filename="tax_report.csv")