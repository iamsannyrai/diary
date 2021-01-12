import uuid
from diary import db


class User(db.Model):
    id = db.Column(db.String(), primary_key=True, default=uuid.uuid4().hex)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.email}')"

    @classmethod
    def find_user_by_email(cls, email):
        return User.query.filter(User.email == email).first()

    @classmethod
    def find_user_by_id(cls, user_id):
        return User.query.filter(User.id == user_id).first()

