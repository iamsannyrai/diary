from marshmallow import Schema, fields, post_load
from diary.models.user import User
from diary import bcrypt


class UserSchema(Schema):
    class Meta:
        model = User

    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)

    """ @post_load decorator deserialize to an object.
        Here make_user() is automatically called
        when instance of this schema is created.
        eg: user = UserSchema().load()
    """

    @post_load
    def make_user(self, data, **kwargs):
        data['password'] = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        return User(**data)