from diary.resources.registration import UserRegistration
from diary.resources.user import UserResource, SingleUserResource
from diary.resources.login import LoginResource


def initialize_routes(api):
    api.add_resource(UserRegistration, '/register')
    api.add_resource(UserResource, '/users')
    api.add_resource(SingleUserResource, '/user/<string:user_id>')
    api.add_resource(LoginResource, '/login')
