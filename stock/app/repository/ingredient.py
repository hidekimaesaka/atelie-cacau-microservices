from app.database import session
from app.models.ingredient import Ingredient

class IngredientRepository:
    @staticmethod
    def create_ingredient(ingredient):
        session.add(ingredient)
        session.commit()
        return ingredient

    @staticmethod
    def get_ingredient(ingredient_id):
        return session.query(Ingredient).get(ingredient_id)

    @staticmethod
    def update_ingredient(ingredient_id, name=None, purchase_date=None, expiration_date=None, package_quantity=None, volume=None, weight=None, supplier_id=None, purchase_price=None):
        ingredient = session.query(Ingredient).get(ingredient_id)
        if ingredient:
            if name:
                ingredient.name = name
            if purchase_date:
                ingredient.purchase_date = purchase_date
            if expiration_date:
                ingredient.expiration_date = expiration_date
            if package_quantity is not None:
                ingredient.package_quantity = package_quantity
            if volume is not None:
                ingredient.volume = volume
            if weight is not None:
                ingredient.weight = weight
            if supplier_id is not None:
                ingredient.supplier_id = supplier_id
            if purchase_price is not None:
                ingredient.purchase_price = purchase_price
            session.commit()
        return ingredient

    @staticmethod
    def delete_ingredient(ingredient):
        session.delete(ingredient)
        session.commit()
        return True

    @staticmethod
    def get_all_ingredients():
        return session.query(Ingredient).all()
