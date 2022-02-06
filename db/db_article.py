import re
from sqlalchemy.orm.session import Session
from exceptions import StoryException
from schemas import ArticleBase 
from db.models import DbArticle
from fastapi import HTTPException,status


def create_article(db: Session, request: ArticleBase):
    if request.content.startwith('Once upon a time'):
        raise StoryException('No stories please')
    new_article= DbArticle(
        title = request.title,
        description =request.description,
        published  = request.published,
        user_id = request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article  

def get_all_article(db: Session):
    return db.query(DbArticle).all()

def get_article(db: Session, id: int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    #handle errors
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {id} not found")
    return article

def update_article(db: Session, request: ArticleBase, id: int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    article.update({
        DbArticle.title : request.title,
        DbArticle.description :request.description,
        DbArticle.published  : request.published,
        DbArticle.user_id : request.creator_id
    })
    db.commit()
    return 'ok'  


def delete_article(db: Session, id: int):
    article = db.query(DbArticle).filter(DbArticle.id == id ).first()

    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {id} not found")
    db.delete(article)
    db.commit()
    return "ok"