from store.controller.category import Category
from store.controller.product import Product


class Home():

    def __init__(self, db):
        self.db = db

    def get_data(self):
        
        product = Product(self.db)
        category = Category(self.db)

        rs1 = category.get_category()
        rs2 = product.get_product()
        
        return rs1, rs2
        
