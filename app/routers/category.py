from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from app.schemas.category import Category
from app.services.category import CategoryService



router = APIRouter()

@router.get('/categories', tags=['setting'])
def get_categories():
    db = Session()
    result = CategoryService(db).get_categories()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))