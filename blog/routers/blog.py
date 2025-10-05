from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, schemas, database, oauth2
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

get_db = database.get_db

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):   
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.Blog, )
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):  
    return blog.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.Blog)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_one(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_one(id, db)
