from app import app, db
from sqlalchemy import text

with app.app_context():
    try:
        db.session.execute(text("ALTER TABLE timetable ADD COLUMN department VARCHAR(50)"))
        db.session.commit()
        print("Added department column to timetable.")
    except Exception as e:
        print(f"Column department already exists or error: {e}")
    
    try:
        db.session.execute(text("ALTER TABLE timetable ADD COLUMN semester INTEGER"))
        db.session.commit()
        print("Added semester column to timetable.")
    except Exception as e:
        print(f"Column semester already exists or error: {e}")
