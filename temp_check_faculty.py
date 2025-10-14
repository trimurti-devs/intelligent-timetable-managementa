from app import app, db, Faculty

with app.app_context():
    faculties = Faculty.query.all()
    for f in faculties:
        print(f"Faculty: {f.name}, Availability: {f.availability}")
