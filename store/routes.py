from flask import Flask, render_template

from store import app
from store import db

from store.controller.category import Category
from store.controller.product import Product

@app.route("/")
def index():
    
    product = Product(db)
    category = Category(db)

    rs1 = category.get_category()
    rs2 = product.get_product()        


    
    return render_template("home.html", category=rs1, product=rs2)
