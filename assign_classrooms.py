from app import app, db, Course, Classroom

with app.app_context():
    courses = Course.query.filter_by(department='ece', semester=7).all()
    classrooms = Classroom.query.all()
    
    print(f"Available classrooms: {[c.name for c in classrooms]}")
    
    for c in courses:
        if not c.classroom_id:
            # Assign a classroom if available
            available_classroom = next((cl for cl in classrooms if cl.capacity > 0), None)
            if available_classroom:
                c.classroom_id = available_classroom.id
                print(f"Assigned classroom {available_classroom.name} to course {c.name}")
            else:
                print(f"No available classroom for course {c.name}")
    
    db.session.commit()
    print("Assignments saved.")
