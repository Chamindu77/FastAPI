from fastapi import FastAPI, Depends, status
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session, sessionmaker
from fastapi import HTTPException
from typing import List

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED, response_model=schemas.Blog)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, content=request.content)
    if not request.title:
        raise HTTPException(status_code=400, detail="Title is required")
    if not request.content:
        raise HTTPException(status_code=400, detail="Content is required")
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"message": "Blog deleted successfully"}

@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.Blog)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with id {id} not found")
    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    return blog.first()

@app.get('/blog', status_code=status.HTTP_200_OK, response_model=List[schemas.Blog])
def get_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=404, detail="No blogs found")
    return blogs

@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.Blog)
def get_one(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with id {id} not found")
    return blog