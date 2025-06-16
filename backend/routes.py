from app import app, db
from flask import request, jsonify
from models import User

import bcrypt


@app.route("/", methods=['GET'])
def home():
    return "<h1> Simulacion laboral </h1>"

@app.route("/api/users", methods=["GET"])
def get_all_users():
    users = User.query.all()
    serialized_users =  [person.serialize() for person in users]
    return jsonify(serialized_users), 200

@app.route("/api/register", methods =["POST"])
def register():
    name = request.json.get("name", None)
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if name ==None:
        return jsonify({"msg": "Missing name"}), 401
    if email ==None:
        return jsonify({"msg": "Missing email"}), 401
    if password ==None:
        return jsonify({"msg": "Missing password"}), 401
    if '@' not in email:
        return jsonify({"msg": "Email must contain '@'."}), 400
    if len(password) <= 6:
        return jsonify({"msg": "Password must have more than 6 characters"}), 400
    
    user = User.query.filter_by(email=email).first()

    if user != None:
        return jsonify({"msg": "El usuario ya existe!"}), 401
    
    bpassword = bytes(password, 'utf-8')
    salt = bcrypt.gensalt(14)

    hashed_password = bcrypt.hashpw(password=bpassword, salt=salt)

    new_user = User(name=name, email=email, password=hashed_password.decode('utf-8'), salt=salt)
    db.session.add(new_user)
    db.session.commit()

    
    return jsonify({"user": new_user.serialize()
                    }),200