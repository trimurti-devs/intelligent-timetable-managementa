from app import app, db, Faculty

with app.app_context():
    # Update sjm
    sjm = Faculty.query.filter_by(name='sjm').first()
    if sjm:
        sjm.availability = 'Mon,Wed,Fri 10:00-16:00'
    
    # Update srs
    srs = Faculty.query.filter_by(name='srs').first()
    if srs:
        srs.availability = 'Mon,Wed,Fri 10:00-16:00'
    
    db.session.commit()
    print("Availability updated for sjm and srs to 'Mon,Wed,Fri 10:00-16:00'")
