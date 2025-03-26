from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from middleware.auth import check_jwt_middleware
from routes.auth import auth_bp
from routes.protected import protected_bp

app = Flask(__name__)
app.config.from_object(Config)

JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(protected_bp)

@app.before_request
def before_request():
    return check_jwt_middleware()

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=False)