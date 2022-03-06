from store import db
from store import app
from flask import session, request
from store.forms.home import FormHome
from store.controller.home import Home
from store.controller.temp import Temp

@app.route("/", methods=["GET", "POST"])
def home():
    return Home(db, session, request, FormHome()).home()
    
@app.route("/product/<int:id>", methods=["GET", "POST"])
def product(id):
    return Home(db, session, request, FormHome()).product(id)

@app.route("/temp", methods=["GET", "POST"])
def temp():
    return Temp(db, session, request, FormHome()).temp(1234)