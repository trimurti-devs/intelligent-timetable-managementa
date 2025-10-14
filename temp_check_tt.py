from app import app, db, Timetable

with app.app_context():
    tts = Timetable.query.all()
    for tt in tts:
        print(f'ID:{tt.id}, Course:{tt.course.name}, Faculty:{tt.faculty_obj.name}, Day:{tt.day}, Time:{tt.start_time}-{tt.end_time}, Dept:{tt.department}, Sem:{tt.semester}')
