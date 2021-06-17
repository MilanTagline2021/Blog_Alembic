from sqlalchemy import create_engine, engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import false


SQLACHEMY_DATABASE_URL = 'sqlite:///./blog_data.db'

engine = create_engine(SQLACHEMY_DATABASE_URL,connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()