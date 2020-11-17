from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from db import db

from resources.user import UserRegister,OneUser,UsersList
from resources.item import Item,ItemList
from resources.store import Store,StoreList



app = Flask(__name__)
db.init_app(app)

app.secret_key = "mash"
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # can be anything 'mysql:///database_new.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
# app.config["JWT_AUTH_URL_RULE"] = '/login'  ,,change /auth ==> /login


@app.before_first_request #decorator affects the method below it,and runs the method before the first rqst
def create_table():
    db.create_all() #before the first request no matter which it is, it wil run this method to create data.db unless already exists

jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister,"/register")

api.add_resource(OneUser,"/user/<string:name>")
api.add_resource(UsersList,"/users")

api.add_resource(Item,"/item/<string:name>")
api.add_resource(ItemList,"/items")

api.add_resource(Store,"/store/<string:name>")
api.add_resource(StoreList,"/stores")


if __name__ == "__main__":
    app.run(port=5000, debug=True)

