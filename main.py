from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/")
def index():
    return {'data':'blog list'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id:int):
    return {'data': f'comments for blog {id}'}

class Blog(BaseModel):
    title: str
    body: str
    author: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'blog is created with title {request.title}'}
