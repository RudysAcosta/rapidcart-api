from fastapi import ApiRouter
from typing import List
from app.schemas.category import Category

router = ApiRouter()

@router.get('/categories', response_model=List[Category], status_code=200, tags=['Category'])
def get_categories() -> List[Category]:
    return 

