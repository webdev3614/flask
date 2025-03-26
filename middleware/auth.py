from flask import request, jsonify

def check_jwt_middleware():
    if request.endpoint not in ['login', 'register']:
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            jsonify({"error":"Missing Authorization Header"}), 401