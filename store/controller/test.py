from flask import render_template
from store.controller.base import Base
from store.models.category import Category as category

class Test(Base):

    def __init__(self, db, session=None, request=None, form=None):
        super().__init__(db, session, request, form)

    def do(self):
        # return "Teste"
        return render_template("test.html", param=123)