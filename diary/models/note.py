import uuid
from datetime import datetime
from diary import db


class Note(db.Model):
    id = db.Column(db.String(), primary_key=True, default=uuid.uuid4().hex)
    title = db.Column(db.String(80), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    note = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.String(), db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Note('{self.title}','{self.user_id}')"

    @classmethod
    def find_note_by_id(cls, note_id):
        return Note.query.filter(Note.id == note_id).first()

    @classmethod
    def find_notes_by_user(cls, user_id):
        return Note.query.filter(Note.user_id == user_id).all()
