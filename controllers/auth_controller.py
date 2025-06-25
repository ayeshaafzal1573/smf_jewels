from passlib.context import CryptContext
from datetime import datetime
from models.user_model import user_helper

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)
