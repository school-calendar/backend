from datetime import datetime, timedelta
from typing import Any, Dict
import jwt
from dotenv import load_dotenv, find_dotenv
import os
from fastapi.security import OAuth2PasswordBearer

load_dotenv(find_dotenv())

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: Dict[str, Any] = {}, expires_delta: timedelta = None) -> str:
	to_encode = data.copy()
	expire = datetime.now() + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
	to_encode.update({"exp": expire})
	return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
