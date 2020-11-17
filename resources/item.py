import sqlite3
from flask_restful import reqparse,Resource
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser() #initializes a new object which we can use to parse the request
    parser.add_argument('price',
            type=float,
            required=True, # ensure no request comes in with no price
            help="This field can't be left blank"
            )
    parser.add_argument('store_id',
            type=int,
            required=True, # ensure no request comes in with no price
            help="Every item needs a store ID."
            )
    
    # @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": f"Item '{name}' Not Found!"},400

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message':f"An item with the name '{name}' already exists"},400

        data = Item.parser.parse_args() 
        item = ItemModel(name,**data)  #data['price'], data['store_id']

        try:
            item.save_to_db()
        except:
            return {'message': 'An Error occured inserting'},500 #internal server Error
        return item.json(),201
    
    # @jwt_required()
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": f"Item '{name}' deleted"}
        return {"message": f"Item '{name}' Not Found"}
        
    def put(self,name):
        data = Item.parser.parse_args() #parse all args that get thru the json payload and put the valid ones in data

        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name,**data)  #data['price'], data['store_id']
        else:
            item = ItemModel(name,data['price'],data['store_id'])
        
        item.save_to_db()
        return item.json()
    

class ItemList(Resource):
    #@jwt_required()
    def get(self):
        return {"items":[item.json() for item in ItemModel.query.all()]} #getting all the  items and iterating thru