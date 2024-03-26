from datetime import datetime 
from app.models.category import Category as CategoryModel
from app.schemas.category import Category
from sqlalchemy.exc import IntegrityError


class CategoryService():

    def __init__(self, db) -> None:
        self.db =  db

    def get_categories(self):
        return self.db.query(CategoryModel).all()
    
    def get_category(self, id: int):
        return self.db.query(CategoryModel).filter(CategoryModel.id == id).first()
    
    def create(self, data: Category):
        try:
            category = CategoryModel(**vars(data))
            self.db.add(category)
            self.db.commit()
        except IntegrityError as e:
            raise Exception(f"Ocurrió un error de integridad: {str(e.orig)}")
        
        return category
        
    def update(self, id, data: Category):
        category = self.db.query(CategoryModel).filter(CategoryModel.id == id).first()

        # if not category break de def
        if not category:
            return None
        
        category.name = data.name
        category.image = data.image
        category.updatedAt = datetime.now()

        self.db.commit()

        return category
        
        
        
        
