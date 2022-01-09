from src.db import db

class Product(db.Model):
    
    def __init__(self, category_id, name, description, amount, price, discount):
        self.category_id = category_id
        self.name = name
        self.description = description
        self.amount = amount
        self.price = price
        self.discount = discount
    
    __tablename__ = "tb_product"
    
    id = db.Column(db.Integer, primary_key = True)
    category_id = db.Column(db.Integer, db.ForeignKey("tb_category.id"), nullable=False)
    name = db.Column(db.String(50), unique = True)
    description = db.Column(db.Text, unique = False)
    amount = db.Column(db.Float, unique = False)
    price = db.Column(db.Float, unique = False)
    discount = db.Column(db.Float, unique = False)
    
    info = db.relationship("ProductInfo", backref="product", lazy=True)
    picture = db.relationship("ProductPicture", backref="product", lazy=True)

    
    def __str__(self):
        return f"Product: Category {self.category_id}, Name {self.name}, Description {self.description}, Amount {self.amount}, Price {self.price}, Discount {self.discount}"


