from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(getenv('SQLALCHEMY_DATABASE_URI'), echo=True)

Base = declarative_base()

def get_session():
    Session = sessionmaker(bind=engine)
    return Session()

def create_all_tables():
    Base.metadata.create_all(engine)

session = get_session()
