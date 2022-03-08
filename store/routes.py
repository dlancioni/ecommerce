from store import db
from store import app
from flask import session, request
from store.forms.home import FormHome
from store.controller.home import Home
from store.controller.cart import Cart
from store.controller.temp import Temp

# Store related routes
@app.route("/", methods=["GET", "POST"])
def home():
    form = FormHome()
    return Home(db, session, request, form).home()

@app.route("/product/<int:id>", methods=["GET", "POST"])
def product(id):
    return Home(db, session, request, FormHome()).product(id)

# Cart related routes
@app.route("/cart", methods=["GET", "POST"])
def cart():
    return Cart(db, session, request, FormHome()).cart()

@app.route("/addcart", methods=["GET", "POST"])
def addcart():
    return Cart(db, session, request, FormHome()).add_cart()

@app.route("/remove_cart/<int:id>", methods=["GET", "POST"])
def remove_cart(id):
    return Cart(db, session, request, FormHome()).remove_cart(id)

# Temporary things
@app.route("/temp", methods=["GET", "POST"])
def temp():
    return Temp(db, session, request, FormHome()).temp(1234)