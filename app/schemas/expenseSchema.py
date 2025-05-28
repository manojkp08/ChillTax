from fastapi import Header
from pydantic import BaseModel

class ExpenseAdd(BaseModel):
    amount: float 
    description: str

class TestingExpenseAdd(BaseModel):
    
    description: str = "Test expense"