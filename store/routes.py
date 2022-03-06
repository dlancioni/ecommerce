from store import db
from store import app
from flask import session, request
from store.forms.store import FormStore
from store.controller.store import Store

@app.route("/", methods=["GET", "POST"])
def home():
    return Store(db, session, request, FormStore()).home()
    
@app.route("/product/<int:id>", methods=["GET", "POST"])
def product(id):
    return Store(db, session, request, FormStore()).product(id)