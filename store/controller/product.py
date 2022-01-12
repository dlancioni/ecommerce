from store import db
from sqlalchemy import and_, or_

from store.controller.base import Base
from store.models.category import Category as c
from store.models.product import Product as p
from store.models.product_info import ProductInfo
from store.models.product_picture import ProductPicture

class Product(Base):

    def __init__(self, db, session=None, request=None, form=None):
        super().__init__(db, session, request, form)
        
    def get_total_product_by_category(self):
        rs = db.session.query(c.name, db.func.count(p.id).label("total")).join(p).group_by(c.name)
        return rs        

    def get_product_by_category(self, category_id = 0):
        rs = p.query.filter(p.category_id == category_id).all()
        return rs

    def get_product(self, description = ""):
        v = "%" + description + "%"
        rs = p.query.filter(or_(p.name.like(v), p.description.like(v))).all()
        return rs