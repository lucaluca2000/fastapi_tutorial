import re
from types import new_class
from sqlalchemy.orm.session import Session
from schemas import ArticleBase 
from db.models import DbArticle


def create_article(db: Session, request: ArticleBase):
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

def get_article(db: Session,id: int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    #handle errors
    return article