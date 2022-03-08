from flask import render_template
from store.controller.base import Base

class Cart(Base):
    
    def __init__(self, db, session=None, request=None, form=None):
        super().__init__(db, session, request, form)
        self.products = []
        
    def add(self, id, name, qtt, price):
        self.products.append([id, name, qtt, price])

    def remove(self, id):
        for index, value in enumerate(self.products):
            if value[0] == id:
                self.products.pop(index)
                return        

    def add_cart(self):
        self.products = self.session['CART_IN']
        self.add(1, "product 1", self.form.quantity, 10.99)
        self.session['CART_IN'] = self.products
        return render_template("home.html", form=self.form)
    