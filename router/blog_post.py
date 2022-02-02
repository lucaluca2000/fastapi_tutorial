
from ast import alias
import datetime
from typing import Optional, List
from fastapi import  status, Response
from pydantic import BaseModel

from fastapi import APIRouter, Query, Body, Path

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)
class Image(BaseModel):
    url: str
    alias: str
class Blog(BaseModel):
    title: str
    description : str = None
    time_publish : datetime.datetime
    comment_id = int
    published : Optional[bool]
    tags: List[str] = []
    image: Optional[Image] = None
@router.post(
    '/new/{blog_id}',
    response_model=Blog,
    summary="create post blog",
    response_description="create blog is successful"
        )
async def create_blog(blog_id: int , blog: Blog, response: Response):

    """
    Create a Blog with all the information's

    - **title**: each blog must have title
    - **description** : a long description
    - **time_publish** : a time publish
    - **tags** : a set unique tag strings for this blog

    """
    if blog.title != "string":
        response.status_code=status.HTTP_200_OK
        result =  {"blog_id": blog_id, **blog.dict()}
        if blog_id != 0:
            result.update({'blog_id': blog_id})
        return result
    else:
        response.status_code = status.HTTP_204_NO_CONTENT


@router.put('/{blog_id}')
async def create_blog(blog_id: int , blog: Blog, response: Response):
    if blog.title != "string":
        response.status_code=status.HTTP_201_CREATED
        return {"blog_id": blog_id, **blog.dict()}
    else:
        response.status_code = status.HTTP_204_NO_CONTENT

    
# @router.post('/{id}/comment/{comment.id}')
# def create_comment(blog: Blog, id: int, 
#     comment_title: int = Query(None,
#         title = 'Title of the Comment',
#         description = 'Some des for comment title',
#         alias = "comment title",
#         deprecated=True
#         ),
#         content: str = Body(...,
#         min_length=3,
#         max_length=50,
#         regex='^[a-z\s]*$',
#         ),
#         v: Optional[List[str]] = Query(['1.1','1.2','1.3']),
#         comment_id: int = Path(None, le=10)
#     ):
#     return {
#         'blog': blog,
#         'id': id,
#         'comment_id': comment_title,
#         'content': content,
#         'version': v,
#         'comment_id': comment_id,

#     } 
@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: Blog, id: int, 
        comment_title: int = Query(None,
            title='Title of the comment',
            description='Some description for comment_title',
            alias='commentTitle',
            deprecated=True
        ),
        content: str = Body(...,
            min_length=10,
            max_length=50,
            regex='^[a-z\s]*$'
        ),
        v: Optional[List[str]] = Query(['1.0', '1.1', '1.2']),
        comment_id: int = Path(None, le=5)
    ):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'content': content,
        'version': v,
        'comment_id': comment_id
    }


def required_functionality():
  return {'message': 'Learning FastAPI is important'}