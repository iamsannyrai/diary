from marshmallow import Schema, fields, post_load
from diary import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.email}')"


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
        return User(**data)
