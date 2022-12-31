from flask import Flask, render_template
from flask.blueprints import Blueprint
from src.db.config import db

from src.models.person import Person
from src.models.person_document import PersonDocument
from src.models.document import Document


home = Blueprint("home", __name__, template_folder = "../templates", static_folder="static")

@home.route("/")
def main():
    
    # Filter
    rs1 = Person.query.filter_by(name = 'David Lancioni').first()      
    
    # Join Person x PersonDocument
    name = PersonDocument.query.all()[0].Person.name    
    Person.query.all()[0].Documents[0].number
        
    Print(Person.query.all()[0].Documents[0].Document.name)
    Print(Person.query.all()[0].Documents[0].number)
    
    # all
    rs1 = Person.query.all()
       
    
    return render_template("home.html", category=rs1, product=rs1)
