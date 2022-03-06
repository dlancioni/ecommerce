from store import db
from flask import render_template, session, request
from store.controller.base import Base
from store.controller.product import Product

class Home(Base):

    def __init__(self, db, session=None, request=None, form=None):
        super().__init__(db, session, request, form)
       
    def home(self):
        category_id = self.request.args.get("category_id", type = int) or 0
        search = self.form.searchbar.data or ""
        rs1, rs2 = Product(db).get_data(category_id, search)
        return render_template("store.html", action = "list", 
                                             form = self.form,
                                             category = rs1,
                                             products = rs2)
        
    def product(self, id):
        rs1, rs2 = Product(db).get_product_details(id)
        return render_template("store.html", action = "product",
                                             form = self.form,
                                             category = rs1, 
                                             product = rs2)