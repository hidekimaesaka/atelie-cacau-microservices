from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from app.database import Base

class Ingredient(Base):
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    purchase_date = Column(Date, nullable=False)
    expiration_date = Column(Date, nullable=False)
    package_quantity = Column(Integer, nullable=False)
    volume = Column(Float)
    weight = Column(Float)
    supplier_id = Column(Integer, ForeignKey('supplier.id'), nullable=False)
    purchase_price = Column(Float, nullable=False)

    def __init__(self, data):
        self.name = data.get('name')
        self.purchase_date = data.get('purchase_date')
        self.expiration_date = data.get('expiration_date')
        self.package_quantity = data.get('package_quantity')
        self.volume = data.get('volume')
        self.weight = data.get('weight')
        self.supplier_id = data.get('supplier_id')
        self.purchase_price = data.get('purchase_price')
