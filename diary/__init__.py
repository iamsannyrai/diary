from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import config

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object(config)
jwt = JWTManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)

from diary.routes import initialize_routes
initialize_routes(api)



