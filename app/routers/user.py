from fastapi import APIRouter,Depends,status
from .. import schema,models,database
from typing import List
from sqlalchemy.orm import Session
# from ..hashing import Hash
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.get('/',response_model=List[schema.PrintUser])
def all(db:Session = Depends(database.get_db)):
    return user.get_all(db)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_user(request:schema.UserIn,db:Session = Depends(database.get_db)):
    return user.create_user(request,db)

@router.get('/{id}',status_code=200,response_model=schema.PrintUser)
def show_user_by_id(id:int,db:Session = Depends(database.get_db)):
    return user.show_user_by_id(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_user(id:int,request:schema.UserIn,db:Session = Depends(database.get_db)):
    return user.update_user(id,request,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int,db: Session=Depends(database.get_db)):
    return user.delete_user(id,db)
