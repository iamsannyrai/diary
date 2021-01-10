from flask import json
from flask_restful import Resource,request,reqparse
from diary.models.user import User,UserSchema
from diary import db


parser = reqparse.RequestParser()
parser.add_argument('username',help='This field cannot be empty',required=True)
parser.add_argument('email',help='This field cannot be empty',required=True)
parser.add_argument('password',help='This field cannot be empty',required=True)

user_schema = UserSchema()

class UserRegistration(Resource):
    def post(self):
        data = request.json
        print(type(data))
        user = User(**data) 
        db.session.add(user)
        db.session.commit()
        # data = parser.parse_args()
        # print(data['username'])
        # data = user_schema.validate(request.json)
        print(f'user is {user.user_json()}')
        return user.user_json()
        # # get request object
        # req_data = request.data
        # # parse
        # user_payload = json.loads(req_data)
        # username = user_payload["username"]
        # email = user_payload["email"]
        # password = user_payload["password"]
        # # store in db
        # new_user = User(username= username,email=email,password=password)
        # db.session.add(new_user)
        # db.session.commit()
        # # return user info
        # return {"username": username, "email": email, "password": password}, 201