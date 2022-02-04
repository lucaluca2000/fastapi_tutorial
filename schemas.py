from pydantic import BaseModel
from typing import List


#Article inside UserDisplay
class Article(BaseModel):
    title: str
    description: str
    published: bool
    class Config():
        orm_mode = True
    # user_id = Column(Integer,ForeignKey('users.id'))
    # user = relationship('DbUser', back_populates='items')

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []
    class Config():
        orm_mode = True
#user inside ArticleDisplay

class User(BaseModel):
    id: int
    username: str
    class Config():
        orm_mode = True

class ArticleBase(BaseModel):
    title: str
    description: str
    published: bool
    creator_id: int


class ArticleDisplay(BaseModel):
    title: str
    description: str
    published: bool
    user:User
    class Config():
        orm_mode = True
