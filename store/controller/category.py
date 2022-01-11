from store.controller.base import Base
from store.models.category import Category as category

class Category(Base):

    def __init__(self, db, session=None, request=None, form=None):
        super().__init__(db, session, request, form)

    def get_category(self):
        rs = category.query.order_by(category.name).all()
        return rs