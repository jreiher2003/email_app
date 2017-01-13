from app import db 

class Unsubscribe(db.Model):
    __tablename__ = "unsub"

    id = db.Column(db.Ineger, primary_key=True)
    email = db.Column(db.String)