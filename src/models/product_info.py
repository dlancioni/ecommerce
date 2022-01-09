from src.db import db

class ProductInfo(db.Model):
    
    def __init__(self, product_id, key, value):
        self.product_id = product_id
        self.key = key
        self.value = value
    
    __tablename__ = "tb_product_info"
    
    id = db.Column(db.Integer, primary_key = True)
    product_id = db.Column(db.Integer, db.ForeignKey("tb_product.id"), nullable=False)    
    key = db.Column(db.String(100), unique = False)
    value = db.Column(db.Text, unique = False)

    def __str__(self):
        return f"ProductInfo: Product {self.product_id}, Key {self.key}, Value {self.value}"


