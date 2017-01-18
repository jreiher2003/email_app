from app import db, uploaded_photos

class Unsubscribe(db.Model):
    #db emails 
    __tablename__ = "unsub"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)

class Export_32(db.Model):
    __bind_key__ = "linkedin"
    __tablename__ = 'export_32'

    # id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, primary_key=True)
