import uuid
from diary import db
from diary.models.note import Note


class User(db.Model):
    id = db.Column(db.String(), primary_key=True, default=uuid.uuid4().hex)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    notes = db.relationship('Note', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.email}', '{self.notes}')"

    @classmethod
    def find_user_by_email(cls, email):
        return User.query.filter(User.email == email).first()

    @classmethod
    def find_user_by_id(cls, user_id):
        return User.query.filter(User.id == user_id).first()

