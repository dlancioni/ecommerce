from store.controller.base import Base

from store.models.product import Product as product
from store.models.product_info import ProductInfo
from store.models.product_picture import ProductPicture

class Product(Base):

    def __init__(self, db, session=None, request=None, form=None):
        super().__init__(db, session, request, form)

    def get_product(self):
        rs = self.db.session.query(product).all()
        return rs