import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv

load_dotenv()

enviroment = os.environ.get('ENVIRONMENT', 'development')

DB_NAME = os.environ.get('DB_NAME', 'db_rapidcart')
DB_USER_NAME = os.environ.get('DB_USER_NAME', 'user_rapidcart')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'pass_rapidcart')
DB_HOST = os.environ.get('DB_HOST', 'localhost')


# TODO: Create a database connection for text database

database_url = f"mysql+mysqlconnector://{DB_USER_NAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(database_url)

Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass