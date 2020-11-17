from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True) # tell sqlalchemy theres a column named ID of type integer & is a PK
    name = db.Column(db.String(255))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer,db.ForeignKey('stores.id'))
    stores = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self): # returns a json rep of the item obj i.e a dictionary
        return {
            'name':self.name,
            'price': self.price,
            'store_id': self.store_id
            }

    @classmethod
    def find_by_name(cls,name):
       return ItemModel.query.filter_by(name=name).first() # SELECT * FROM __tablename__(items) WHERE name=name LIMIT=1

    def save_to_db(self):
       db.session.add(self)
       db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()