from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


SQLalchemy_DATABASE_URL= "sqlite:///movies.db"

engine = create_engine(SQLalchemy_DATABASE_URL,connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

class Base(DeclarativeBase):
    pass