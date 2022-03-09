from flask import render_template
from store.controller.base import Base

class Cart(Base):
    
    def __init__(self, db, session=None, request=None, form=None):
        super().__init__(db, session, request, form)
        self.products = []
        
    def create(self, form):        
        id = int(form["id"])
        name = str(form["name"])
        qtt = int(form["quantity"])
        price = float(form["price"])
        total = float(qtt * price)
        product = [id, name, qtt, price, total]
        return product

    def add(self, product):
        if self.find(product[0]) == -1:
            self.products.append(product)

    def remove(self, id):
        index = self.find(id)
        if index >= 0:
            self.products.pop(index)

    def find(self, id):
        for index, value in enumerate(self.products):
            if int(value[0]) == int(id): 
                return index
        return -1

    def cart(self):
        self.products = self.session['CART_IN']
        return render_template("cart.html", form=self.form, cart_in=self.products)

    def add_cart(self):        
        self.products = self.session['CART_IN']
        product = self.create(self.request.form)
        self.add(product)
        self.session['CART_IN'] = self.products
        return render_template("cart.html", form=self.form, cart_in=self.products)

    def remove_cart(self, id):
        self.products = self.session['CART_IN']
        self.remove(id)
        self.session['CART_IN'] = self.products
        return render_template("cart.html", form=self.form, cart_in=self.products)