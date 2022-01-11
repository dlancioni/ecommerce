from flask import Flask, render_template, session, request

from store import app
from store import db
from store.controller.home import Home


@app.route("/", methods=["GET"])
def index():
    
    home = Home(db, session, request)
    rs1, rs2 = home.get_data()
    
    return render_template("home.html", category=rs1, products=rs2)
