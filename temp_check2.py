from app import app, db, Course, Faculty
with app.app_context():
    courses = Course.query.all()
    for c in courses:
        faculty_name = c.faculty.name if c.faculty else 'None'
        print(f"{c.name}: {faculty_name}")
