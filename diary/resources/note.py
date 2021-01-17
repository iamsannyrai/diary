from flask_restful import Resource, request
from marshmallow import ValidationError

from diary import db
from diary.models.note import Note
from diary.schemas.note_schema import NoteSchema
from diary.utils.jwt_utils import JWTUtils

notes_schema = NoteSchema(many=True)
note_schema = NoteSchema()


class SaveNote(Resource):
    def post(self):
        try:
            decoded = JWTUtils.decode(request.headers['Authorization'])
            if decoded is not None:
                note = note_schema.load(request.json)
                db.session.add(note)
                db.session.commit()
                return note_schema.dump(note)
            else:
                return {
                           'status': 401,
                           'message': 'Invalid token'
                       }, 401
        except ValidationError as e:
            return e.messages


class NotesResource(Resource):
    def get(self):
        decoded = JWTUtils.decode(request.headers['Authorization'])
        if decoded is not None:
            all_notes = Note.query.all()
            return notes_schema.dump(all_notes)
        else:
            return {
                       'status': 401,
                       'message': 'Invalid token'
                   }, 401


class AllNotesByUserResource(Resource):
    def get(self, user_id):
        decoded = JWTUtils.decode(request.headers['Authorization'])
        if decoded is not None:
            all_notes = Note.find_notes_by_user(user_id)
            return notes_schema.dump(all_notes)
        else:
            return {
                       'status': 401,
                       'message': 'Invalid token'
                   }, 401


class SingleNoteResource(Resource):
    def get(self, note_id):
        decoded = JWTUtils.decode(request.headers['Authorization'])
        if decoded is not None:
            note = Note.find_note_by_id(note_id)
            return note_schema.dump(note)
        else:
            return {
                       'status': 401,
                       'message': 'Invalid token'
                   }, 401
