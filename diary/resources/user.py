from flask_restful import Resource
from diary.models.user import User
from diary.schemas.user_schema import UserSchema


users_schema = UserSchema(many=True, only=('username', 'email'))
user_schema = UserSchema(only=('username', 'email'))


class UserResource(Resource):
    def get(self):
        all_users = User.query.all()
        return users_schema.dump(all_users)


class SingleUserResource(Resource):
    def get(self, user_id):
        user = User.find_user_by_id(user_id)
        return user_schema.dump(user)
