from sqlalchemy import Column, Integer, String
from src.db.config import db

class Document(db.Model):
    __tablename__ = 'tb_document'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
