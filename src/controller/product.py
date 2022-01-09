from re import DEBUG
from src.models.product import Product as product

class Product():

    def __init__(self, db):
        self.db = db

    def get_product(self):
        rs = self.db.session.query(product).all()
        return rs