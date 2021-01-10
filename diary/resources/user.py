from flask_restful import Resource
from diary.models.user import User, UserSchema


users_schema = UserSchema(many=True)
user_schema = UserSchema()


class UserResource(Resource):
    def get(self):
        all_users = User.query.all()
        return users_schema.dump(all_users)


class SingleUserResource(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        return user_schema.dump(user)
