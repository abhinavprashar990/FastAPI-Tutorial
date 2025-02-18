from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from .schemas import TokenData



SECRET_KEY = "AbhinavPrashar123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id : int = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(id = user_id)
        return token_data
    except JWTError:
        raise credentials_exception