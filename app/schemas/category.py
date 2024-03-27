from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class Category(BaseModel):
    id: Optional[int] = None
    name: str
    image: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

    products: List['Product'] = []

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Clothes",
                "image": "https://i.imgur.com/QkIa5tT.jpeg",
                "createdAt": "2024-03-18T05:09:12.000Z",
                "updatedAt": "2024-03-18T05:09:12.000Z"
            }
        }

from .product import Product