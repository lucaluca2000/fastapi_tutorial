from typing import List
from fastapi import APIRouter, Depends
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay, UserBase 
from sqlalchemy.orm import Session
from db import db_article
from auth.oauth2 import get_current_user, oauth2_scheme
router = APIRouter(
    prefix='/article',
    tags=['article']
)

# Create article
@router.post('/', response_model= ArticleDisplay)  
def create_article(request: ArticleBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
    'data': db_article.create_article(db, request),
    'current_user': current_user
    } 
# Get all article
@router.get('/',response_model=List[ArticleDisplay])
def get_article(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
    'data': db_article.get_article(db),
    'current_user': current_user
    } 
# Get specific article
@router.get('/{id}')#,response_model= ArticleDisplay)
def get_all_article(id:int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
    'data': db_article.get_article(db, id),
    'current_user': current_user
    } 