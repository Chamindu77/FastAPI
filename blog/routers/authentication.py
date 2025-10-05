from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models, token
from ..hashing import Hashing
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from ..repository import authentication

get_db = database.get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# @router.post('/login')
# def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.email == request.username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username")
#     if not Hashing.verify_password(request.password, user.password):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    
#     access_token = token.create_access_token(data={"sub": user.email})
#     return {"access_token": access_token, "token_type": "bearer"}

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return authentication.login(db, request)