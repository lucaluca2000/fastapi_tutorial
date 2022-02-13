from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
# from passlib.context import CryptContext
from datetime import datetime, timedelta


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

SECRET_KEY = "4bc3a4b1b5b9668366351c31c7b0f76a38e6d054b5fd72aa93dee0dde49ba38c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta = None ):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
