from flask_restful import reqparse,Resource
#from flask_jwt import jwt_required
from models.store import StoreModel


class Store(Resource):
    def get(self,name): 
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message":f"The store '{name}' is Not Found."}
    
    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message':f"A store with the name '{name}' already exists"},400
        # data = Store.parser.parse_args(name,)
        store = StoreModel(name)
        try:
            store.save_to_db()
            # return{"message":"store created successfully"},201
        except:
            return {"message": "An error creating the store"},500
        return store.json()

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {"message":" Store Deleted."}
        return {"message":" Store Not Found."}

class StoreList(Resource):
    def get(self):
        return {"stores":[store.json() for store in StoreModel.query.all()]}