from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLalchemy_DATABASE_URL= "sqlite:///todos.db"

engine = create_engine(SQLalchemy_DATABASE_URL,connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()