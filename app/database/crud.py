from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.auth.models import User
from app.expenses.models import Expense
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD Operations
def get_user(db: Session, email_or_username: str, password: str):
    return db.query(User).filter(
        (User.email == email_or_username) | (User.username == email_or_username),
        User.password == password
    ).first()

def create_user(db: Session, name: str, email: str, username: str, password: str, phone: str):
    user = User(name=name, email=email, username=username, password=password, phone=phone)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def add_expense(db: Session, user_id: int, amount: float, description: str, category: str, tax_relevant: bool):
    expense = Expense(user_id=user_id, amount=amount, description=description, category=category, tax_relevant=tax_relevant)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

def get_expenses(db: Session, user_id: int):
    return db.query(Expense).filter(Expense.user_id == user_id).all()