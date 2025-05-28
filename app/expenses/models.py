from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, ForeignKey
from app.database.base import Base

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    description = Column(String)
    category = Column(String)
    tax_relevant = Column(Boolean)
    date = Column(DateTime)