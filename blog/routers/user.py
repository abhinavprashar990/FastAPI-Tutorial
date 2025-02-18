from fastapi import APIRouter,Depends, HTTPException, status, Response
from .. import database,schemas,models
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user



router = APIRouter(
    prefix='/user',
    tags=['users']
)


get_db = database.get_db



@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request,db)



@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int, db:Session=Depends(get_db)):
    return user.get_user(id,db)