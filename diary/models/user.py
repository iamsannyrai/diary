import uuid,random
from flask_marshmallow import fields
from diary import db, ma
from diary.validators import set_attributes


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.email}')"
    
    def __init__(self,**kwargs):
        super().__init__()
        self.id = random.randint(1,100)
        set_attributes(self,**kwargs)
    
    def user_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password
        } 

    allowed_keys = {'username','email','password'}


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

    # username = fields.Str(required=True)
