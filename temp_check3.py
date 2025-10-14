from app import app, db, Timetable
with app.app_context():
    timetables = Timetable.query.all()
    for tt in timetables:
        print(f"{tt.day} {tt.start_time} - {tt.end_time} {tt.course.name} {tt.faculty_obj.name} {tt.classroom_obj.name}")
