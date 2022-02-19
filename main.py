from fastapi.exceptions import HTTPException
from fastapi import FastAPI, Request
from exceptions import StoryException
from router import  blog_get, blog_post, user, article, product, file
from auth import authentication
from db import models,database
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from templates import templates
app = FastAPI()

origins= [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)
app.include_router(templates.router)
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(file.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={"detail": f"Oops! {exc.name} did something.  There goes a rainbow..."},
    )

@app.exception_handler(HTTPException)
def custom_handler(request: Request, exc: StoryException):
    return PlainTextResponse(str(exc), status_code=400)


models.Base.metadata.create_all(database.engine)



app.mount('/files', StaticFiles(directory="files"), name='files')
app.mount('/templates/static', StaticFiles(directory="templates/static"), name='static')