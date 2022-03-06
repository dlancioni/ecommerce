from store import db
from flask import render_template, session, request
from store.forms.store import FormStore
from store.controller.base import Base
from store.controller.category import Category
from store.controller.product import Product


class Store(Base):

    def __init__(self, db, session=None, request=None, form=None):
        super().__init__(db, session, request, form)
       
    def home(self):
        form1 = FormStore()
        store = Store(db, session, request, form1)
        rs1, rs2 = store.get_data()
        return render_template("store.html", action = "list", 
                                             form_home = form1, 
                                             category = rs1, 
                                             products = rs2)
        
    def product(self, id):
        form1 = FormStore()
        store = Store(db, session, request, form1)
        rs1, rs2 = store.get_product_details(id)
        return render_template("store.html", action = "product",
                                             form_home = form1,
                                             category = rs1, 
                                             product = rs2)        

    def get_data(self):       
        product = Product(self.db)        
        category_id = self.request.args.get("category_id", type = int) or 0
        description = self.form.searchbar.data or ""
        rs1 = product.get_total_product_by_category()                
        rs2 = product.get_product_by_category(category_id) if category_id > 0 else product.get_product(description)
        return rs1, rs2
    
    def get_product_details(self, id): 
        product = Product(self.db)
        rs1 = product.get_total_product_by_category()
        rs2 = product.get_product_by_id(id)
        return rs1, rs2    