from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database
from sqlalchemy.orm import Session
from typing import List
from ..repository import user


router = APIRouter(
    prefix="/user",
    tags = ['User']
)

get_db = database.get_db



@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
def get_all_users(db: Session = Depends(get_db)):
  return user.get_all(db) 

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_one_user(id: int, db: Session = Depends(get_db)):
    return user.get_one(id, db) 