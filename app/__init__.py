from flask import Flask
from app.auth import auth_bp
from app.bcrypt import bcrypt


def create_app():


    app=Flask(__name__)
    app.register_blueprint(auth_bp,url_prefix="/auth")
    bcrypt.init_app(app)
    return app