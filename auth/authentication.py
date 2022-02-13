from ctypes.wintypes import DWORD
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.database import get_db
from pydantic import BaseModel
from db import models
from db.hash import Hash
from auth import oauth2

router = APIRouter(
    tags=['authentication']
)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str  = None


@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.DbUser).filter(models.DbUser.username == request.username).first()
    if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid credentials")
    if not Hash.verify(user.password , request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid credentials")
    
    access_token = oauth2.create_access_token(data={'sub': user.username})

    return{
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user.id,
        'username': user.username
    }