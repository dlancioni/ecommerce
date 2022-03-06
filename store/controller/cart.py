from flask import render_template
from store.controller.base import Base

class Cart(Base):

    def __init__(self, db, session=None, request=None, form=None):
        super().__init__(db, session, request, form)

    def add_cart(self):
        return "Adiconado no carrinho:" + str(self.form.quantity)