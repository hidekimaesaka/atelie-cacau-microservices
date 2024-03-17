from sqlalchemy import Column, Integer, String, Float, Date

from app.database import Base

class Product(Base):

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    expiration_date = Column(Date, nullable=False)
    manufacture_date = Column(Date, nullable=False)
    weight = Column(Float, nullable=False)

    def __init__(self, data):
        self.name = data.get('name')
        self.quantity = data.get('quantity')
        self.price = data.get('price')
        self.expiration_date = data.get('expiration_date')
        self.manufacture_date = data.get('manufacture_date')
        self.weight = data.get('weight')
