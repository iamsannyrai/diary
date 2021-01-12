from flask_restful import Resource, request
from marshmallow import ValidationError
from diary.schemas.user_schema import UserSchema
from diary import db


user_load_schema = UserSchema()
user_schema = UserSchema(only=('username', 'email'))


class UserRegistration(Resource):
    def post(self):
        try:
            user = user_load_schema.load(request.json)
            db.session.add(user)
            db.session.commit()
            return user_schema.dump(user)
        except ValidationError as e:
            return e.messages
