from fastapi import APIRouter, Depends
from fastapi import status, Response
from enum import Enum
from typing import Optional
from router.blog_post import required_functionality 
router = APIRouter(
    prefix='/blog',
    tags=['blog']
)



@router.get("/")
async def root():
    return {"message": "Hello World"}



fake_db = [{'item_name': 'alexnet'},{ 'item_name' : 'resnet'},{'item_name' : 'lenet'}]

@router.get('/all/{id}',status_code=status.HTTP_200_OK)
def get_all_blogs(page = 1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
  return {'message': f'All {page_size} blogs on page {page}', 'req': req_parameter}

@router.get('/{id}',status_code=status.HTTP_200_OK)
def get_blogs(id: int,response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        
        return {'message': f'Blog with id {id}'}

class ModelsName(str,Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

# @router.get("/items/",tags=['items'])
# def read_items(skip: int= 0,limit : int = 10):
#     return fake_db[skip : skip+limit]

@router.get(
    "/type/{model_name}",
    tags=['blog'],
    summary="Retrive type blog",
    description="This api call simulates fetching type blog"
    )
async def get_all_blogs(model_name : ModelsName):
    if model_name == ModelsName.alexnet:
        return {"model_name" : model_name}
    elif model_name == ModelsName.resnet:
        return {"model_name" : model_name}
    elif model_name == ModelsName.lenet:
        return {"model_name" : model_name}


@router.get('/{id}/comments/{comment_id}',tags=['comment'])
def get_comment(id: int ,comment_id : int, valid : bool = True, username: Optional[str] = None):
    return {'message' : f'blog id {id} , comment id {comment_id} , valid {valid}, username {username}'}
