from pydantic import BaseModel, EmailStr
from typing import List

class Blog(BaseModel):
    title: str
    content: str
        
class User(BaseModel):
    username: str
    email: EmailStr
    password: str
 
class ShowUser(BaseModel):
    username: str
    email: EmailStr
    blogs : List[Blog]

    class Config():
        orm_mode = True

class ShowUserInBlog(BaseModel):
    username: str
    email: EmailStr

    class Config():
        orm_mode = True

class ShowBlog(Blog):
    id: int
    title: str
    content: str
    creator: ShowUserInBlog

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None