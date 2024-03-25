from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import Session, engine, Base
from app.models.category import Category as CategoryModel
from app.routers import category as category_router


app = FastAPI()
app.title = "Rapidcart Api"
app.version = "0.0.1"

app.include_router(category_router.router)


Base.metadata.create_all(bind=engine)


@app.get('/', tags=['Home'])
def read_root():
    return {"Hello": "World"}