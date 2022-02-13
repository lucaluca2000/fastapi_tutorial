from typing import List
from fastapi import APIRouter, Depends
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay 
from sqlalchemy.orm import Session
from db import db_article
from auth.oauth2 import oauth2_scheme
router = APIRouter(
    prefix='/article',
    tags=['article']
)

# Create article
@router.post('/', response_model= ArticleDisplay)  
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)

# Get all article
@router.get('/',response_model=List[ArticleDisplay])
def get_article(db: Session = Depends(get_db)):
    return db_article.get_article(db)

# Get specific article
@router.get('/{id}',response_model= ArticleDisplay)
def get_all_article(id:int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return db_article.get_article(db, id)