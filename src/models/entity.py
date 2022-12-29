from sqlalchemy.ext.automap import automap_base

class Entity():

    def __init__(self, db):
        self.db = db

    def get_class(self):        
        Base = automap_base()
        Base.prepare(self.db.engine, reflect=True)
        return Base.classes.tb_person