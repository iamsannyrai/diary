from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
ma = Marshmallow(app)

api = Api(app)

from diary.routes import initialize_routes
initialize_routes(api)



