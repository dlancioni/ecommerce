from src.models.person import Person

class Person():

    def __init__(self, db):
        self.db = db
        
    def get_list(self):

        rs = self.db.query(Person).all()
        for row in rs:
            print(row.name)
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