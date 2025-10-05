from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from blog import models, schemas, database
from . import token


db = database.SessionLocal()


outh2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(data: str = Depends(outh2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.verify_access_token(data, credentials_exception)
    