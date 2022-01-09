from src.db import db

class ProductPicture(db.Model):
    
    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name
    
    __tablename__ = "tb_product_picture"
    
    id = db.Column(db.Integer, primary_key = True)
    product_id = db.Column(db.Integer, db.ForeignKey("tb_product.id"), nullable=False)    
    name = db.Column(db.Text, unique = False)

    def __str__(self):
        return f"ProductPicture: Product {self.product_id}, Name {self.name}"


