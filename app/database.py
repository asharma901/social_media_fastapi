import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

#create DB url in below format:
# url_name = 'postgresql://<db_username>:<db_pwd>@<ip-addr/hostname>/<db_name>'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

#engine is responsible for establishing connection to db
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#session is responsible for talking to db
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#below code is when we use postgres driver directly and not alchemy
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='admin', cursor_factory= RealDictCursor)
#         cursor = conn. cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print(f"Database connection has failed. Error: {error}")
#         time.sleep(2)