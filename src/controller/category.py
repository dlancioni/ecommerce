from src.models.category import Category as category

class Category():

    def __init__(self, db):
        self.db = db

    def get_category(self):
        rs = category.query.order_by(category.name).all()
        return rs