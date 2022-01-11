from store import db

class Category(db.Model):
       
    def __init__(self, id, name):
        self.id = id
        self.name = name

    __tablename__ = "tb_category"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    products = db.relationship("Product", backref="category", lazy=True)
    
    def __str__(self):
        return f"Category: Name {self.name}"
