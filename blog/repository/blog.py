from blog.oauth2 import get_current_user
from fastapi import status,HTTPException
from sqlalchemy.orm.session import Session
from .. import models,schema,oauth2

def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request:schema.Blog,db:Session):
    new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
    # print(get_current_user)
    db.add(new_blog)
    db. commit()
    db.refresh(new_blog)
    return new_blog    

def destroy(id:int,db:Session):
        blogs = db.query(models.Blog).filter(models.Blog.id == id)
        if not blogs.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} is not found')
        blogs.delete(synchronize_session=False)
        db.commit()
        return "Deleted succeessfully"
    
def update(id:int,request:schema.Blog,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} is not found')
    blog.update(request.dict())
    db.commit()
    return "Updated succeessfully"

def show(id:int,db:Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} is not available' )
    return blogs