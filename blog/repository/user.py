from fastapi import status,HTTPException
from sqlalchemy.orm.session import Session
from .. import models,schema
from ..hashing import Hash

def get_all(db:Session):
    users = db.query(models.User).all()
    return users

def create_user(request:schema,db:Session):
    detail = models.User(username=request.username,password=Hash.bcrypt(request.password),email=request.email)
    db.add(detail)
    db.commit()
    db.refresh(detail)
    return detail  

def show_user_by_id(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with id {id} is not available' )
    return user
    
def update_user(id:int,request:schema.UserIn,db:Session):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with id {id} is not found')
    user.update(request.dict())
    db.commit()
    return "Updated succeessfully"

def delete_user(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with id {id} is not found')
    user.delete(synchronize_session=False)
    db.commit()
    return "Deleted succeessfully"
