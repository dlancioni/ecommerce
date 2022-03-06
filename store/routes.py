from flask import Flask, render_template, session, request

from store import db
from store import app
from store.controller.store import Store

@app.route("/", methods=["GET", "POST"])
def home():
    return Store(db, session, request).home()
    
@app.route("/product/<int:id>", methods=["GET", "POST"])
def product(id):
    return Store(db, session, request).product(id)