from store import db
from flask import render_template
from store.controller.base import Base
from store.controller.product import Product
from store.controller.cart import Cart

class Home(Base):

    def __init__(self, db, session=None, request=None, form=None):
        super().__init__(db, session, request, form)
        if not self.session.get('CART_IN'):
            self.session['CART_IN'] = []        
       
    def home(self):
        category_id = self.request.args.get("category_id", type=int) or 0
        search = self.form.searchbar.data or ""
        rs1, rs2 = Product(db).get_data(category_id, search)
        return render_template("home.html", form=self.form, category=rs1, products=rs2)

    def product(self, id):
        qtt = 1       
        product, index = Cart(db, self.session).find(id)
        if product != []:
            qtt = product[2]
        rs1, rs2 = Product(db).get_product_details(id)
        return render_template("product.html", form=self.form, category=rs1, product=rs2, qtt=qtt)