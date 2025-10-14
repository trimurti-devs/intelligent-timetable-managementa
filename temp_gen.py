from app import app, db, generate_timetable, Course
with app.app_context():
    courses = Course.query.all()
    schedulable = [c for c in courses if c.faculty_id and c.classroom_id]
    print("Schedulable courses:")
    for c in schedulable:
        print(f"{c.name} {c.faculty.name if c.faculty else 'None'}")
    result = generate_timetable(schedulable)
    print(f"Generation result: {result}")
