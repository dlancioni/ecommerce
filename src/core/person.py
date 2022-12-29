from src.models.entity import Entity
from sqlalchemy.ext.automap import automap_base

class Person():

    def __init__(self, db):
        self.db = db
        
    def query(self):
        tb_person = Entity(self.db).get_class()
        rs = self.db.session.query(tb_person).all()
        for row in rs:
            print(row.name)
            print(row.tb_person_document_collection[0].number)
        return rs

    def save(self):
        item = self.Person(id=3, ds="Other types...")
        self.db.session.add(item)
        self.db.session.commit()

    def delete(self):
        Person = Model.get(self.db)
        item = self.db.session.query(Person).get(1)
        self.db.session.delete(item)
        self.db.session.commit()