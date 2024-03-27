from typing import List
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.sql import func
from config.database import Base

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name = Column(String(100), nullable= False, unique=True)
    image = Column(String(100))
    createdAt = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True), onupdate=func.now())

    products: Mapped[List["Product"]] = relationship(cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Category {self.id} = {self.name}>"