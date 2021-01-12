from flask_restful import Resource, request
from marshmallow import ValidationError
from diary.models.user import User
from diary.schemas.login_schema import LoginSchema
from diary import bcrypt

login_schema = LoginSchema()


class LoginResource(Resource):
    def post(self):
        try:
            credential = login_schema.load(request.json)
            user = User.find_user_by_email(credential['email'])
            if user:
                is_correct = bcrypt.check_password_hash(user.password, credential['password'])
                if is_correct:
                    return {"username": user.username, "email": user.email}, 200
                else:
                    return {"message": "Invalid Credential"}, 400
            else:
                return {"message": "No user found with given email"}, 400
        except ValidationError as e:
            return e.messages
