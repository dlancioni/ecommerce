from flask import render_template
from store.controller.base import Base

class Temp(Base):

    def __init__(self, db, session=None, request=None, form=None):
        super().__init__(db, session, request, form)

    def temp(self, value):
        return render_template("temp.html", param=value)