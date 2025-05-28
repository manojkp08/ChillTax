from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.expenses.router import router as expenses_router
from app.donations.router import router as donations_router
from app.export.router import router as export_router

app = FastAPI()
app.include_router(auth_router, prefix="/auth")
app.include_router(expenses_router, prefix="/expenses")
app.include_router(donations_router, prefix="/donations")
app.include_router(export_router, prefix="/export")

@app.get("/")
def root():
    return {"message": "Tax Fighter API"}