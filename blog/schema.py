from typing import List, Optional
from pydantic import BaseModel


class BlogBase(BaseModel):
    title : str
    body : str

class Blog(BlogBase):
    class Config():
        orm_mode = True 

class UserIn(BaseModel):
    username: str
    password: str
    email: str

    class Config:
        orm_mode = True

class PrintUser(BaseModel):
    username: str
    email: str
    blogs : List[Blog]

    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    title : str
    body : str
    creator : PrintUser

    class Config():
        orm_mode = True

    
class Login(BaseModel):
    email : str
    password : str

class Tocken(BaseModel):
    access_token : str
    token_type : str 

class TokenData(BaseModel):
    email : Optional[str] = None