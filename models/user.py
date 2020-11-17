#import sqlite3
from db import db


class UserModel(db.Model): # this class now has the ability to interact with sqlite3
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # tell sqlalchemy theres a column named ID of type integer & is a PK
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        return UserModel.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls,_id):
        return UserModel.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def json(self): # necessary to hide your password though
        return {
            'username':self.username
            }