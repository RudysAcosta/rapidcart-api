from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.schemas.category import Category


class Product(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3, max_length=100)
    price: float = Field(..., gt=0)
    description: Optional[str] | None = Field(None, max_length=500)
    images: List[str] 
    creationAt: datetime | None
    updatedAt: datetime | None

    category: Category

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Black T-Shirt",
                "price": 25.00,
                "description": "A black t-shirt",
                "images": ["https://i.imgur.com/QkIa5tT.jpeg"],
                "creationAt": "2024-03-18T05:09:12.000Z",
                "updatedAt": "2024-03-18T05:09:12.000Z",
                "category": {
                    "id": 1,
                    "name": "Clothes",
                    "image": "https://i.imgur.com/QkIa5tT.jpeg",
                    "creationAt": "2024-03-18T05:09:12.000Z",
                    "updatedAt": "2024-03-18T05:09:12.000Z"
                }
            }
        }


external_data = {
    "id": 1,
    "title": "Black T-Shirt",
    "price": 25.00,
    "description": "A black t-shirt",
    "images": ["https://i.imgur.com/QkIa5tT.jpeg"],
    "creationAt": "2024-03-18T05:09:12.000Z",
    "updatedAt": "2024-03-18T05:09:12.000Z",
    "category": {
        "id": 1,
        "name": "Clothes",
        "image": "https://i.imgur.com/QkIa5tT.jpeg",
        "creationAt": "2024-03-18T05:09:12.000Z",
        "updatedAt": "2024-03-18T05:09:12.000Z"
    }
}