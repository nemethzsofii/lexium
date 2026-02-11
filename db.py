# db.py
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

APP_NAME = "Lexium"

def get_appdata_path():
    base_path = os.getenv("LOCALAPPDATA")
    app_path = os.path.join(base_path, APP_NAME)
    os.makedirs(app_path, exist_ok=True)
    return app_path

def init_db(app):
    appdata_path = get_appdata_path()
    db_path = os.path.join(appdata_path, "database.db")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()