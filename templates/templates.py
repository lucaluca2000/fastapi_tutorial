from fastapi import APIRouter, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from schemas import ProductBase
from custom_log import log
router = APIRouter(
    prefix='/templates',
    tags=['templates']
)

templates = Jinja2Templates(directory="templates")
 

@router.post("/products/{id}", response_class=HTMLResponse)
def post_product(
        id: str,
        product: ProductBase, 
        request:Request,
        bt:BackgroundTasks
        ):
    bt.add_task(log_template_call,f"tempalate for product with id {id}")
    return templates.TemplateResponse(
            "product.html",
            {
                "request":request,
                "id":id,
                "title":product.title,
                "description":product.description,
                "price": product.price

            }
        )

def log_template_call(message: str):
    log("MyAPI", message)