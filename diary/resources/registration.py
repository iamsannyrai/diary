from flask_restful import Resource, request
from marshmallow import ValidationError
from diary.models.user import UserSchema, user_only_attributes
from diary import db

user_schema = UserSchema(only=user_only_attributes)
user_load_schema = UserSchema()


class UserRegistration(Resource):
    def post(self):
        try:
            user = user_load_schema.load(request.json)
            db.session.add(user)
            db.session.commit()
            return user_schema.dump(user)
        except ValidationError as e:
            return e.messages
