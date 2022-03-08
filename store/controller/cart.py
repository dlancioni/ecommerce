from flask import render_template
from store.controller.base import Base

class Cart(Base):
    
    def __init__(self, db, session=None, request=None, form=None):
        super().__init__(db, session, request, form)
        self.products = []
        
    def add(self, id, name, qtt, price):
        if self.find(id) == -1:
                self.products.append([id, name, qtt, price])

    def remove(self, id):
        for index, value in enumerate(self.products):
            if value[0] == id:
                self.products.pop(index)
                return
            
    def find(self, id):
        for index, value in enumerate(self.products):
            if value[0] == id: 
                return index
        return -1

    def cart(self):
        self.products = self.session['CART_IN']        
        return render_template("cart.html", form=self.form, cart_in=self.products)

    def add_cart(self):
        self.products = self.session['CART_IN']
        id = self.request.form["id"]
        name = self.request.form["name"]
        quantity = self.request.form["quantity"]
        price = self.request.form["price"]        
        self.add(id, name, quantity, price)
        self.session['CART_IN'] = self.products
        return render_template("cart.html", form=self.form, cart_in=self.products)
    