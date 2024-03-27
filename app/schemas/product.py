from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from .category import Category


class Product(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3, max_length=100)
    price: float = Field(..., gt=0)
    description: Optional[str] | None = Field(None, max_length=500)
    category_id: int

    category:  Optional[Category] = None
    
    creationAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Black T-Shirt",
                "price": 25.00,
                "description": "A black t-shirt",
                "creationAt": "2024-03-18T05:09:12.000Z",
                "updatedAt": "2024-03-18T05:09:12.000Z"
            }
        }