from app import app, db
from flask import request, jsonify
from models import User

@app.route("/api/users", methods=["GET"])
def get_all_users():
    users = User.query.all()
    serialized_users =  [person.serialize() for person in users]
    return jsonify(serialized_users), 200