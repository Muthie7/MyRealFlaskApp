import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="this field cant be blank!"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="this field cant be blank!"
    )

    def post(self): #this will be called when we post some data to User REgister endpoint
        data = UserRegister.parser.parse_args() #parse the args in variable data as JSON 
        if UserModel.find_by_username(data['username']): #user =(1,'bob','asdf) is what is returned
            return{"message": f"The user with the username '{data['username']}' already exists."},403

        user = UserModel(**data) #{data['username'],data['password']} and since its a dict we use **kwargs
        user.save_to_db()
        return {"message":"User created successfully"},201

    
class UsersList(Resource):
    def get(self):
        return{"users":[user.json() for user in UserModel.query.all()]}

class OneUser(Resource):
    def get(self,name):
        user = UserModel.find_by_username(name)
        if user:   
            return user.json()
        else:
            return{"message":f"The user '{name}' Not Found"}

    def delete(self,name): #DEBUG
        user = UserModel.find_by_username(name)
        if user:
            user.delete_from_db()
            #return{"message":"User deleted"}
        return{"users":[x.json() for x in UserModel.query.all()]}
       
    
