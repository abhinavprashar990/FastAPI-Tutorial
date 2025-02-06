from fastapi import APIRouter
from .. import schemas,database, models
from typing import List
from fastapi import FastAPI, Depends, HTTPException, status, Response
from . import schemas, models
from .. database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/user', response_model=schemas.ShowUser,tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return request

@router.get('/user/{id}',response_model=schemas.ShowUser, tags=['users'])
def get_user(id:int, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    return user