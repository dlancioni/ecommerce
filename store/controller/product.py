from store.models.product import Product as product
from store.models.product_info import ProductInfo
from store.models.product_picture import ProductPicture

class Product():

    def __init__(self, db):
        self.db = db

    def get_product(self):
        rs = self.db.session.query(product).all()
        return rs