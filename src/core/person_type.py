from re import DEBUG
from sqlalchemy.ext.automap import automap_base

class PersonTypes():

    def __init__(self, db):
        self.db = db
        Base = automap_base()
        Base.prepare(db.engine, reflect=True)
        self.PersonType = Base.classes.tb_person_type
        
    def save(self):        
        
        item = self.PersonType(id=3, ds="Other types...")
        self.db.session.add(item)
        self.db.session.commit()

    def get_list(self):        
        rs = self.db.session.query(self.PersonType).all()
        for item in rs:
            print(item.ds)
        return rs