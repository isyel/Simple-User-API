from flask import Flask
from config import Config
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
mail = Mail(app)

from application import routes

from .commands import db_create, db_drop, db_seed

app.cli.add_command(db_create)
app.cli.add_command(db_drop)
app.cli.add_command(db_seed)