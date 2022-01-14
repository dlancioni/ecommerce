from store.controller.base import Base
from store.controller.category import Category
from store.controller.product import Product


class Store(Base):

    def __init__(self, db, session=None, request=None, form=None):
        super().__init__(db, session, request, form)

    def get_data(self):
        
        product = Product(self.db)        
        category_id = self.request.args.get("category_id", type = int) or 0
        description = self.form.searchbar.data or ""
        rs1 = product.get_total_product_by_category()
        
        if category_id > 0:
            rs2 = product.get_product_by_category(category_id)
        else:
            rs2 = product.get_product(description)

        return rs1, rs2
    
    def get_product_details(self, id): 
        product = Product(self.db)
        rs1 = product.get_total_product_by_category()
        rs2 = product.get_product_by_id(id)
        return rs1, rs2    