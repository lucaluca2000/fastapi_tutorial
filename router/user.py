from typing import List
from webbrowser import get
from fastapi import APIRouter, Depends
from db.database import get_db
from schemas import UserBase, UserDisplay 
from sqlalchemy.orm import Session
from db import db_user
from auth.oauth2 import get_current_user, oauth2_scheme

router = APIRouter(
    prefix='/user',
    tags=['user']
)


#Create user

@router.post('/', response_model= UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

#Read all user
@router.get('/',response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
    'data':  db_user.delete_user(db),
    'current_user': current_user
    } 
#Read one user
@router.get('/{id}',response_model=UserDisplay)
def get_one_user(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
    'data':  db_user.get_user(db, id),
    'current_user': current_user
    } 
    
# Update user 
@router.post('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
    'data':  db_user.update_user(db, id, request),
    'current_user': current_user
    } 
#Delete user
@router.get('/delete/{id}/')
def delete_user(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
    'data':  db_user.delete_user(db, id),
    'current_user': current_user
    } 