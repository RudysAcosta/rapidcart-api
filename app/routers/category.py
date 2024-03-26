from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from app.schemas.category import Category
from app.services.category import CategoryService
from app.models.category import Category as CategoryModel
from sqlalchemy.exc import IntegrityError


router = APIRouter()

@router.get('/categories', tags=['setting'])
def get_categories():
    db = Session()
    result = CategoryService(db).get_categories()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.get('/categories/{id}', tags=['setting'], status_code=200)
def get_category(id: int):
    db = Session()
    result = CategoryService(db).get_category(id)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.post('/categories', tags=['setting'], response_model=Category, status_code=201)
def create_category(category: Category):
    db = Session()
    try:
        result = CategoryService(db).create(category)
    except Exception as e:
        return JSONResponse(status_code=400, content=jsonable_encoder({'message': str(e)}))

    return JSONResponse(status_code=201, content=jsonable_encoder(result))

@router.put('/categories/{id}', tags=['setting'], status_code=200)
def update_category(id: int, category: Category):
    db = Session()
    
    try:
        result = CategoryService(db).update(id, category)
    except Exception as e:
        return JSONResponse(status_code=400, content=jsonable_encoder({'message': str(e)}))


    return JSONResponse(status_code=200, content=jsonable_encoder(result))
