from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

api = Api(app)

from diary.routes import initialize_routes
initialize_routes(api)



