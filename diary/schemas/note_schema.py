from marshmallow import Schema, fields, post_load
from diary.models.note import Note


class NoteSchema(Schema):
    class Meta:
        model = Note

    id = fields.Str()
    title = fields.Str(required=True)
    note = fields.Str(required=True)
    user_id = fields.Str(required=True)

    @post_load
    def make_note(self, data, **kwargs):
        return Note(**data)