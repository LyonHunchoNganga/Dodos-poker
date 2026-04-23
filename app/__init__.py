from flask import Flask
from app.auth import auth_bp
from app.poker_routes import poker_bp
from app.bcrypt import bcrypt


def create_app():


    app=Flask(__name__)
    app.register_blueprint(auth_bp,url_prefix="/auth")
    app.register_blueprint(poker_bp,url_prefix="/poker")
    bcrypt.init_app(app)
    return app