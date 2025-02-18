from fastapi import APIRouter,Depends, HTTPException
from .. import schemas,database,models,token
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..schemas import Token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Authentication']
)

get_db = database.get_db



@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    
    if not user:
        raise HTTPException(status_code=404, detail=f"Invalid Credentials")
    
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=404, detail=f"Incorrect password")
    

    access_token = token.create_access_token(data={"user_id": user.id}, expires_delta=False)
    
    return Token(access_token=access_token, token_type="bearer")