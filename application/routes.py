from application import app, db, mail
from flask import request, json, jsonify, make_response
from flask_jwt_extended import jwt_required, create_access_token, decode_token

from .models import User, user_schema, users_schema
from random import randint

from flask_mail import Message


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return make_response(jsonify(message='Hello, World, Welcome to Simple Users API!'), 200)


# Register new user
@app.route('/register', methods=['POST'])  
def register():
    email = request.form['email']
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify(message="This email already exists"), 409
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        user = User(first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify(message="User created Successfully"), 201
    

# User login
@app.route('/login', methods=['POST'])  
def login():
    if request.is_json:
        email = request.json['email']
        password = request.json['password']
    else:
        email = request.form['email']
        password = request.form['password']
        
    user = User.query.filter_by(email=email).first()
    if user and user.get_password(password):
        access_token = create_access_token(identity=email)
        return jsonify(message="Login Succeeded", access_token=access_token)
    else:
        return jsonify(message="Wrong email or password"), 401
    
    
# Retreive lost password
@app.route('/retrieve_password/<string:email>', methods=['GET'])  
def retrieve_password(email: str):
    user = User.query.filter_by(email=email).first()
    if user:
        user.reset_code = randint(1000, 9999)
        db.session.commit()
        msg = Message("your password reset code is " + str(user.reset_code),
                      sender="adminfoo@gmail.com",
                      recipients=[email])
        mail.send(msg)
        return jsonify(message="Password Reset Code sent to " + email)
    else:
        return jsonify(message="That email doesn't exist"), 401
    

# Reset password to new password
@app.route('/reset_password', methods=['POST'])  
def reset_password():
    if request.is_json:
        email = request.json['email']
        reset_code = request.json['reset_code']
        new_password = request.json['new_password']
    else:
        email = request.form['email']
        reset_code = request.form['reset_code']
        new_password = request.form['new_password']
        
    user = User.query.filter_by(email=email, reset_code=reset_code).first()
    if user:
        user.set_password(new_password)
        db.session.commit()
        return jsonify(message="Password reset successfully, you can login with new password")
    else:
        return jsonify(message="Your reset code is Incorrect or has Expired"), 401
    
  
# Get list of users  
@app.route('/users', methods=['GET'])  
def users():
    users_list = User.query.all()
    result = users_schema.dump(users_list)
    return jsonify(result)


# get details of single user
@app.route('/users/<int:id>', methods=['GET'])  
def user_details(id: int):
    user = User.query.filter_by(id=id).first()
    if user:
        result = user_schema.dump(user)
        return jsonify(result)
    else:
        return jsonify(message="that user does not exist"), 404
    
    
# get logged in user profile
@app.route('/user-profile', methods=['POST']) 
@jwt_required  
def user_profile():
    token = request.json['access_token']
    decoded_token = decode_token(token)
    email = decoded_token["identity"]
    user = User.query.filter_by(email=email).first()
    if user:
        result = user_schema.dump(user)
        return jsonify(result)
    else:
        return jsonify(message="Sorry, could not find your profile"), 404
    

# Update user details
@app.route('/users', methods=['PUT']) 
@jwt_required 
def update_user():
    id = int(request.form['id'])
    user = User.query.filter_by(id=id).first()
    if user:
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.email = request.form['email']
        db.session.commit()
        return jsonify(message="Profile Updated Successfully")
    else:
        return jsonify(message="This user does not exist"), 404


# Update your profile
@app.route('/update_profile', methods=['PUT']) 
@jwt_required 
def update_profile():
    id = int(request.json['id'])
    user_id = User.query.filter_by(id=id).first()
    if user_id:
        token = request.json['access_token']
        decoded_token = decode_token(token)
        email = decoded_token["identity"]
        user = User.query.filter_by(email=email, id=id).first()
        if user:
            user.first_name = request.json['first_name']
            user.last_name = request.json['last_name']
            user.email = request.json['email']
            db.session.commit()
            return jsonify(message="Profile Updated Successfully")
        else:
            return jsonify(message="Sorry you cannot update this profile"), 404
    else:
        return jsonify(message="This user does not exist"), 404