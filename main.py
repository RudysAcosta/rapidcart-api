import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.title = "Rapidcart Api"
app.version = "0.0.1"

products = []

with open('products.json', 'r') as file:
    products =  json.load(file)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/', tags=['Home'])
def read_root():
    return {"Hello": "World"}

@app.get('/products', tags=['Product'])
def get_products():
    return products


@app.get('/products/{id}', tags=['Product'])
def get_product(id: int):
    product = next((product for product in products if product['id'] == id), None)
    return product

@app.get('/products/{id}/category', tags=['Product'])
def get_products_by_category(category: int):
    products_by_category = list(filter(lambda product: product['category']['id'] == category, products))
    return products_by_category