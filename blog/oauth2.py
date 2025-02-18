from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from . import database
from . import token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")






# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from .models import User
# from .utils import get_user_from_token  # type: ignore # This is just an example of how to fetch the user.

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# def get_current_user(token: str = Depends(oauth2_scheme)):
#     user = get_user_from_token(token)
#     if user is None:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
#     return user




def get_current_user(data:str = Depends(oauth2_scheme), db:Session = Depends(database.get_db)):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    

    return token.verify_token(data ,credentials_exception)

    
    