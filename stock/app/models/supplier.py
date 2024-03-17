from sqlalchemy import Column, Integer, String
from app.database import Base

class Supplier(Base):
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)

    def __init__(self, data):
        self.name = data.get('name')
        self.address = data.get('address')
