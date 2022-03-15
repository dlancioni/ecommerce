import flask
from store import db
from flask import render_template, redirect, url_for
from store.controller.base import Base
from store.controller.product import Product

class Cart(Base):
    
    # Cart definition    
    PRODUCT_ID = 0
    PRODUCT_NAME = 1
    PRODUCT_QTT = 2
    PRODUCT_PRICE = 3
    PRODUCT_TOTAL = 4
    PRODUCT_SOLD_OUT = 5
    
    def __init__(self, db, session=None, request=None, form=None):
        super().__init__(db, session, request, form)
        self.open_cart()
        self.total_shopping = 0
            
    def open_cart(self):
        self.shopping_cart = self.session['CART_IN']
        
    def close_cart(self):
        self.session['CART_IN'] = self.shopping_cart

    def create(self, form):
        id = int(form["id"])
        name = str(form["name"])
        qtt = int(form["quantity"])
        price = float(form["price"])
        total = float(qtt * price)
        sold_out = False
        product = [id, name, qtt, price, total, sold_out]
        return product

    def add(self, new):
        old, _ = self.find(new[self.PRODUCT_ID])
        if old == []:
            self.shopping_cart.append(new)
        else:
            old[self.PRODUCT_QTT] = new[self.PRODUCT_QTT]
            old[self.PRODUCT_PRICE] = new[self.PRODUCT_PRICE]
            old[self.PRODUCT_TOTAL] = old[self.PRODUCT_QTT] * old[self.PRODUCT_PRICE]

    def remove(self, id):
        product, index = self.find(id)
        if product != []:
            self.shopping_cart.pop(index)

    def find(self, id):
        index = 0
        product = []
        for index, value in enumerate(self.shopping_cart):
            if int(value[self.PRODUCT_ID]) == int(id): 
                product = value
                break
        return product, index

    def cart(self):
        self.open_cart()
        category_id = self.request.args.get("category_id", type=int) or 0
        rs1, rs2 = Product(db).get_data(category_id, "")
        self.mark_as_sold_out(rs2)
        self.calculate_total()        
        return render_template("cart.html", form=self.form, cart_in=self.shopping_cart, total=self.total_shopping, category=rs1)

    def add_cart(self):
        if flask.request.method == "POST":
            self.open_cart()
            product = self.create(self.request.form)
            self.add(product)
            self.close_cart()
            return redirect(url_for("list_cart"))

    def remove_cart(self, id):
        self.open_cart()
        self.remove(id)
        self.close_cart()
        return redirect(url_for("list_cart"))
    
    def calculate_total(self):
        self.open_cart()
        total = 0
        for item in self.shopping_cart:
            if  not item[self.PRODUCT_SOLD_OUT]:
                total = total + item[self.PRODUCT_TOTAL]
        self.close_cart()
        self.total_shopping = total

    def mark_as_sold_out(self, products):
        self.open_cart()        
        for item in self.shopping_cart:
            for product in products:
                if int(item[self.PRODUCT_ID]) == int(product.id):
                    if product.amount == 0:
                        item[self.PRODUCT_SOLD_OUT] = True
                    else:
                        item[self.PRODUCT_SOLD_OUT] = False
                    break                        
        self.close_cart()
