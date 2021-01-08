from flask import json
from flask_restful import Resource, request
from diary.models.user import User, UserSchema
from diary import db

users_schema = UserSchema(many=True)
user_schema = UserSchema()


class UserResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)


class SingleUserResource(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        return user_schema.dump(user)
