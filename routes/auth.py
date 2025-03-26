from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email == "admin" and password == "password":
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    return jsonify({"error":"Invalid credentials"}), 401