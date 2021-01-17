from flask import jsonify
from flask_restful import Resource, request
from diary.models.user import User
from diary.schemas.user_schema import UserSchema, UserSchemaFromDb
from diary.utils.jwt_utils import JWTUtils

users_schema = UserSchema(many=True, only=('id', 'username', 'email'))
user_schema = UserSchema(only=('id', 'username', 'email'))
all_db_user_schema = UserSchemaFromDb(many=True)


class UserResource(Resource):
    def get(self):
        decoded = JWTUtils.decode(request.headers['Authorization'])
        if decoded is not None:
            all_users = User.query.all()
            return users_schema.dump(all_users)
        else:
            return {
                       'status': 401,
                       'message': 'Invalid token'
                   }, 401


class SingleUserResource(Resource):
    def get(self, user_id):
        user = User.find_user_by_id(user_id)
        return user_schema.dump(user)
