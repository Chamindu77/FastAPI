from pydantic import BaseModel, EmailStr

class Blog(BaseModel):
    title: str
    content: str

class ShowBlog(Blog):
    id: int
    class Config():
        orm_mode = True
        
class User(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config():
        orm_mode = True
    
class ShowUser(BaseModel):
    username: str
    email: EmailStr

    class Config():
        orm_mode = True