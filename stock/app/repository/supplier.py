from app.database import session
from app.models.supplier import Supplier

class SupplierRepository:
    @staticmethod
    def create_supplier(supplier):
        session.add(supplier)
        session.commit()
        return supplier

    @staticmethod
    def get_supplier(supplier):
        return supplier

    @staticmethod
    def update_supplier(supplier_id, name=None, address=None):
        supplier = session.query(Supplier).filter_by(id=supplier_id).first()
        if supplier:
            if name:
                supplier.name = name
            if address:
                supplier.address = address
            session.commit()
        return supplier

    @staticmethod
    def delete_supplier(supplier):
        session.delete(supplier)
        session.commit()
        return True

    @staticmethod
    def get_all_suppliers():
        return session.query(Supplier).all()
