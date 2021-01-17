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

    def patch(self, note_id):
        decoded = JWTUtils.decode(request.headers['Authorization'])
        if decoded is not None:
            note = note_schema.load(request.json)
            db_note = Note.find_note_by_id(note_id)
            if db_note is not None:
                print(f'before {db_note.title}')
                db_note.title = note.title
                db_note.note = note.note
                db_note.user_id = note.user_id
                print(f'after {db_note.title}')
                db.session.add(db_note)
                db.session.commit()
                return note_schema.dump(db_note)
            else:
                return {
                           'status': 404,
                           'message': 'Note not found'
                       }, 400
        else:
            return {
                       'status': 401,
                       'message': 'Invalid token'
                   }, 401

    def delete(self, note_id):
        decoded = JWTUtils.decode(request.headers['Authorization'])
        if decoded is not None:
            db_note = Note.find_note_by_id(note_id)
            if db_note is not None:
                db.session.delete(db_note)
                db.session.commit()
                return {
                    'status': 200,
                    'message': 'Note deleted successfully'
                }
            else:
                return {
                           'status': 404,
                           'message': 'Note not found'
                       }, 400
        else:
            return {
                       'status': 401,
                       'message': 'Invalid token'
                   }, 401
