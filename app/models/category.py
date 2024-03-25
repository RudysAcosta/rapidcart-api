from sqlalchemy.schema import CreateTable
from sqlalchemy import Column, Integer, String,TIMESTAMP
from sqlalchemy.sql import func
from config.database import Base


class Category(Base):

    __tablename__ = 'categories'
    
    id  =  Column(Integer, primary_key = True)
    name = Column(String(100), nullable= False)
    image = Column(String(100))
    createdAt = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True), onupdate=func.now())
