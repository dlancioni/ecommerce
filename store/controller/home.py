from store.controller.base import Base
from store.controller.category import Category
from store.controller.product import Product


class Home(Base):

    def __init__(self, db, session=None, request=None):
        super().__init__(db, session, request)

    def get_data(self):
        
        product = Product(self.db)
        category = Category(self.db)
        
        category_id = self.request.args.get("category_id")

        rs1 = category.get_category()
        rs2 = product.get_product()
        
        return rs1, rs2
        
