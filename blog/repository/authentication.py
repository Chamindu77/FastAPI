from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas
from ..hashing import Hashing
from .. import token

def login (db: Session, request: schemas.Login):
    #print("USERNAME:", request.username)
    #print("PASSWORD:", request.password)
    user = db.query(models.User).filter((models.User.email == request.username) | (models.User.username == request.username)).first()
    #print("FOUND USER:", user)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username")
    if not Hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
