import os
from mcoc import views
from decouple import config
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = config("DATABASE_URL")
    app.register_blueprint(views.bp)

    return app