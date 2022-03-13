import flask
from store import db
from flask import render_template, redirect, url_for
from store.controller.base import Base
from store.controller.product import Product

class Cart(Base):
    
    def __init__(self, db, session=None, request=None, form=None):
        super().__init__(db, session, request, form)
        self.open_cart()
        self.total = 0        
            
    def open_cart(self):
        self.products = self.session['CART_IN']
        
    def close_cart(self):
        self.session['CART_IN'] = self.products

    def create(self, form):        
        id = int(form["id"])
        name = str(form["name"])
        qtt = int(form["quantity"])
        price = float(form["price"])
        total = float(qtt * price)
        value = 0.0
        product = [id, name, qtt, price, total]
        return product

    def add(self, new):
        old, _ = self.find(new[0])
        if old == []:
            self.products.append(new)
        else:
            old[2] = new[2]
            old[3] = new[3]
            old[4] = old[2] * old[3]

    def remove(self, id):
        product, index = self.find(id)
        if product != []:
            self.products.pop(index)

    def find(self, id):
        index = 0
        product = []
        for index, value in enumerate(self.products):
            if int(value[0]) == int(id): 
                product = value
                break
        return product, index

    def cart(self):
        self.open_cart()
        self.calculate_total()
        category_id = self.request.args.get("category_id", type=int) or 0
        rs1, _ = Product(db).get_data(category_id, "")
        return render_template("cart.html", form=self.form, cart_in=self.products, total=self.total, category=rs1)

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
        for item in self.products:
            total = total + item[4]
        self.close_cart()
        self.total = total
