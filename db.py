from datetime import datetime
import sqlite3

from flask_sqlalchemy import SQLAlchemy
import os
import json
import sys
from pathlib import Path

db = SQLAlchemy()

APP_NAME = "Lexium"

def get_appdata_path():
    base_path = os.getenv("LOCALAPPDATA") or str(Path.home())
    app_path = os.path.join(base_path, APP_NAME)
    os.makedirs(app_path, exist_ok=True)
    return app_path

def get_resource_path(relative_path: str) -> Path:
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / relative_path
    return Path(__file__).parent / relative_path

def load_default_case_types():
    json_path = get_resource_path("static/files/default_case_types.json")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data.get("DEFAULT_CASE_TYPES", [])

def seed_case_types():
    from models import CaseType  # import models here inside function to avoid circular import

    default_case_types = load_default_case_types()

    if not default_case_types:
        print("No default case types found.")
        return

    for name in default_case_types:
        existing = CaseType.query.filter_by(name=name).first()
        if not existing:
            db.session.add(CaseType(name=name, active=1))

    db.session.commit()
    print("Default case types seeded.")

def backup_sqlite_db(db_path: str, max_backups: int = 10):
    backup_dir = os.path.join(get_appdata_path(), "backups")
    os.makedirs(backup_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"database_{timestamp}.db")

    # Use SQLite backup API (safe even if DB is in use)
    source = sqlite3.connect(db_path)
    dest = sqlite3.connect(backup_path)

    with dest:
        source.backup(dest)

    dest.close()
    source.close()

    # Rotate old backups (keep newest 10)
    backups = sorted(
        [f for f in os.listdir(backup_dir) if f.endswith(".db")]
    )

    while len(backups) > max_backups:
        oldest = backups.pop(0)
        os.remove(os.path.join(backup_dir, oldest))

    print("Database backup completed.")

def init_db(app):
    db_path = os.path.join(get_appdata_path(), "database.db")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = False

    db.init_app(app)

    with app.app_context():
        import models # import models here so tables are registered (casetype is known)
        db.create_all()
        if os.path.exists(db_path):
            backup_sqlite_db(db_path)
        seed_case_types()
