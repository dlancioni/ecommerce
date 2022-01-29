from store import db

class ProductPicture(db.Model):
    
    def __init__(self, product_id, name, width, heigth, type):
        self.product_id = product_id
        self.name = name
        self.width = width
        self.heigth = heigth
        self.type = type
    
    __tablename__ = "tb_product_picture"
    
    id = db.Column(db.Integer, primary_key = True)
    product_id = db.Column(db.Integer, db.ForeignKey("tb_product.id"), nullable=False)    
    name = db.Column(db.Text, unique = False)
    width = db.Column(db.String(50))
    heigth = db.Column(db.String(50))
    type = db.Column(db.Integer)

    def __str__(self):
        return f"ProductPicture: Product {self.product_id}, Name {self.name}"


