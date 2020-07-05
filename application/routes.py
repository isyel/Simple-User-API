from application import app, db
from flask import request, json, jsonify, make_response
# from application.models import User


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return make_response(jsonify(message='Hello, World!'), 200)


@app.route("/api")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    return Response(json.dumps(jdata), mimetype="application/json")
