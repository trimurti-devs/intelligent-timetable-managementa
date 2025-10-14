from app import app, db
from sqlalchemy import text

with app.app_context():
    try:
        db.session.execute(text("ALTER TABLE timetable ADD COLUMN generation INTEGER DEFAULT 1"))
        db.session.commit()
        print("Added generation column to timetable.")
    except Exception as e:
        print(f"Column generation already exists or error: {e}")
