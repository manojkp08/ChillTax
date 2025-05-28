from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.auth.models import User
from app.auth.utils import generate_token, verify_password
from app.database.crud import get_db
from app.auth.utils import get_password_hash
from app.schemas.authSchemas import LoginRequest, SignUpRequest

router = APIRouter()

@router.post("/signup")
def signup(payload: SignUpRequest, db: Session = Depends(get_db)):
    if db.query(User).filter((User.email == payload.email) | (User.username == payload.username)).first():
        raise HTTPException(status_code=400, detail="Email or username already registered")

    user = User(
        name=payload.name,
        email=payload.email,
        username=payload.username,
        password=get_password_hash(payload.password),
        phone=payload.phone,
        token=generate_token()
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {'token': user.token}

@router.post("/login")
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(
        (User.email == payload.email_or_username) | 
        (User.username == payload.email_or_username)
    ).first()
    
    if not user or not verify_password(payload.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {'token': user.token}