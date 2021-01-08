from flask import json
from flask_restful import Resource,request
from diary.models.user import User
from diary import db

class UserRegistration(Resource):
    def post(self):
        # get request object
        req_data = request.data
        # parse
        user_payload = json.loads(req_data)
        username = user_payload["username"]
        email = user_payload["email"]
        password = user_payload["password"]
        # store in db
        new_user = User(username= username,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        # return user info
        return {"username": username, "email": email, "password": password}, 201