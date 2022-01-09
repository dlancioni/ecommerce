from src.db import db

class User(db.Model):
    
    def __init__(self, username):
        self.username = username

    __tablename__ = "tb_user"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True)

    def __str__(self):
        return f"User: Username {self.username}"