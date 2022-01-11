from flask import Flask, render_template, session, request

from store import app
from store import db
from store.web.forms.home import FormHome
from store.controller.home import Home


@app.route("/", methods=["GET", "POST"])
def index():
    
    form_home = FormHome()
    home = Home(db, session, request)
    rs1, rs2 = home.get_data()
    
    return render_template("home.html", form_home=form_home, 
                                        category=rs1, 
                                        products=rs2)