from app import app, db, Course

with app.app_context():
    courses = Course.query.filter_by(department='ece', semester=5).all()
    print(f"Number of courses for ECE 5th semester: {len(courses)}")
    for c in courses:
        print(f"Course: {c.name}, Faculty: {c.faculty_id}, Classroom: {c.classroom_id}")
    
    schedulable = [c for c in courses if c.faculty_id and c.classroom_id]
    print(f"Schedulable courses: {len(schedulable)}")
    for c in schedulable:
        print(f"Schedulable: {c.name}")
