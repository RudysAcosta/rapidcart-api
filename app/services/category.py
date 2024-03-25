from app.models.category import Category as CategoryModel
from app.schemas.category import Category

class CategoryService():

    def __init__(self, db) -> None:
        self.db =  db

    def get_categories(self):
        return self.db.query(CategoryModel).all()