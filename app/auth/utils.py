import secrets

from fastapi import HTTPException
from passlib.context import CryptContext

from app.auth.models import User

def generate_token():
    return secrets.token_hex(16)

def validate_token(db, token):
    user = db.query(User).filter(User.token == token).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user.id

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)