from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_raw_jwt
from diary.models.user import User
from diary.schemas.user_schema import UserSchema


users_schema = UserSchema(many=True, only=('username', 'email'))
user_schema = UserSchema(only=('username', 'email'))


class UserResource(Resource):
    @jwt_required
    def get(self):
        all_users = User.query.all()
        return users_schema.dump(all_users)


class SingleUserResource(Resource):
    def get(self, user_id):
        user = User.find_user_by_id(user_id)
        return user_schema.dump(user)
