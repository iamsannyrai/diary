from diary.resources.registration import UserRegistration
from diary.resources.user import UserResource, SingleUserResource
from diary.resources.login import LoginResource
from diary.resources.note import SaveNote, NotesResource, AllNotesByUserResource, SingleNoteResource


def initialize_routes(api):
    api.add_resource(UserRegistration, '/register')
    api.add_resource(UserResource, '/users')
    api.add_resource(SingleUserResource, '/user/<string:user_id>')
    api.add_resource(LoginResource, '/login')
    api.add_resource(SaveNote, '/note')
    api.add_resource(NotesResource, '/notes')
    api.add_resource(AllNotesByUserResource, '/notes/<string:user_id>')
    api.add_resource(SingleNoteResource, '/note/<string:note_id>')
