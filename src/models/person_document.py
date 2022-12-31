from sqlalchemy import Column, Integer, String
from src.db.config import db

class PersonDocument(db.Model):
    __tablename__ = 'tb_person_document'
    
    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, unique=True)
    number = db.Column(db.String(50), unique=True)
    person_id = db.Column(db.Integer, db.ForeignKey('tb_person.id'), nullable=False)
    Person = db.relationship('Person', backref=db.backref('Documents', lazy=True))