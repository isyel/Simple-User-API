import flask
from sqlalchemy import Column, Integer, String, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow
from application import db, ma


# Create user table class
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(25))
    last_name = Column(String(25))
    email = Column(String(35), unique=True)
    password = Column(String(255))
    reset_code = Column(Integer, nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)
    

# create classes for serialization   
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email')
        

# instantiate schema classes, for when single row or returning multiple rows
user_schema = UserSchema()
users_schema = UserSchema(many=True)