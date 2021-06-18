from fastapi import APIRouter,Depends,status
from .. import schema,database,oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

@router.get('/',response_model=List[schema.ShowBlog])
def all(db:Session = Depends(database.get_db),current_user: schema.UserIn=Depends(oauth2.get_current_user)):
    # print(current_user.id)
    return blog.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schema.Blog,db:Session = Depends(database.get_db),current_user: schema.UserIn=Depends(oauth2.get_current_user)):
    return blog.create(request,db) 

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db: Session=Depends(database.get_db),current_user: schema.UserIn=Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)
    
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schema.Blog,db:Session = Depends(database.get_db),current_user: schema.UserIn=Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)

@router.get('/{id}',status_code=200,response_model=schema.ShowBlog)
def show(id:int,db:Session = Depends(database.get_db),current_user: schema.UserIn=Depends(oauth2.get_current_user)):
    return blog.show(id,db)
    
   