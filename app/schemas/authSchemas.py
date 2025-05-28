from pydantic import BaseModel

class SignUpRequest(BaseModel):
    name: str
    email: str
    username: str
    password: str
    phone: str

class LoginRequest(BaseModel):
    email_or_username: str
    password: str