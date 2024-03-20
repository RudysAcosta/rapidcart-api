from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Category(BaseModel):
    id: Optional[int] = None
    name: str
    image: str
    creationAt: datetime | None
    updatedAt: datetime | None

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Clothes",
                "image": "https://i.imgur.com/QkIa5tT.jpeg",
                "creationAt": "2024-03-18T05:09:12.000Z",
                "updatedAt": "2024-03-18T05:09:12.000Z"
            }
        }
