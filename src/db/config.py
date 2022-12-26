# https://docs.sqlalchemy.org/en/14/orm/queryguide.html#select-statements

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
db = SQLAlchemy()
db_url = "mysql+mysqldb://root:admin@localhost/ecommerce"

def create_db(app, db):
    with app.app_context():
        Base = automap_base()
        Base.prepare(db.engine, reflect=True)
