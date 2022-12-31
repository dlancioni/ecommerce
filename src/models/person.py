from sqlalchemy import Column, Integer, String
from src.db.config import db

from src.models.person_document import PersonDocument

class Person(db.Model):
    __tablename__ = 'tb_person'   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    
