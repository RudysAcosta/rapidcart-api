
from typing import List
from sqlalchemy import Column, ForeignKey, Numeric, String, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from config.database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    title = Column(String(100), nullable= False)
    price = Column(Numeric(precision=12, scale=2), nullable= False)
    descrition = Column(String(500))
    
    createdAt = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True), onupdate=func.now())

    category: Mapped["Category"] = relationship()

    def __repr__(self) -> str:
        return f"<Product {self.id} = {self.title}>"