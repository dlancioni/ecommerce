from flask import Flask, render_template, session, request

from store import db
from store import app
from store.forms.store import FormStore
from store.controller.store import Store

@app.route("/", methods=["GET", "POST"])
def index():
    
    form1 = FormStore()
    store = Store(db, session, request, form1)
    rs1, rs2 = store.get_data()
    
    return render_template("store.html", form_home=form1, 
                                         category=rs1, 
                                         products=rs2)