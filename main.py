from fastapi import FastAPI
from router import  blog_get, blog_post, user, article
from db import models,database

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)



models.Base.metadata.create_all(database.engine)



