from flask import Flask, render_template
from flask.blueprints import Blueprint
from src.db.config import db

from src.core.person_type import PersonTypes



home = Blueprint("home", __name__, template_folder = "../templates", static_folder="static")

@home.route("/")
def main():
    
    x = PersonTypes(db)
    
    x.save()
    rs1 = x.get_list()
    
    
    return render_template("home.html", category=rs1, product=rs1)
