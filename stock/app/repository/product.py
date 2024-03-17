from app.database import session
from app.models.product import Product

class ProductRepository:
    @staticmethod
    def create_product(product):
        session.add(product)
        session.commit()
        return product

    @staticmethod
    def get_product(product_id):
        return session.query(Product).get(product_id)

    @staticmethod
    def update_product(product_id, name=None, quantity=None, price=None, expiration_date=None, manufacture_date=None, weight=None):
        product = session.query(Product).get(product_id)
        if product:
            if name:
                product.name = name
            if quantity is not None:
                product.quantity = quantity
            if price is not None:
                product.price = price
            if expiration_date:
                product.expiration_date = expiration_date
            if manufacture_date:
                product.manufacture_date = manufacture_date
            if weight is not None:
                product.weight = weight
            session.commit()
        return product

    @staticmethod
    def delete_product(product):
        session.delete(product)
        session.commit()
        return True

    @staticmethod
    def get_all_products():
        return session.query(Product).all()
