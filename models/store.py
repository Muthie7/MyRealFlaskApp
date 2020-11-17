from db import db
from models.item import ItemModel


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True) # tell sqlalchemy theres a column named ID of type integer & is a PK
    name = db.Column(db.String(255))
    items = db.relationship('ItemModel',lazy='dynamic') #everytime we call the .json() we have to go into the table

    def __init__(self, name):
        self.name = name

    def json(self): # returns a json rep of the item obj i.e a dictionary
        return {
            'name':self.name,
            'items':[item.json() for item in self.items.all()]
            }

    @classmethod
    def find_by_name(cls,name):
       return StoreModel.query.filter_by(name=name).first() # SELECT * FROM __tablename__(stores) WHERE name=name LIMIT=1

    def save_to_db(self):
       db.session.add(self)
       db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()