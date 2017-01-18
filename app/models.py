from app import db, uploaded_photos

class Unsubscribe(db.Model):
    #db emails 
    __tablename__ = "unsub"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)

class Dropbox_Img(db.Model):
    # db emails
    __tablename__ = "dropbox_img"

    id = db.Column(db.Integer, primary_key=True)

    bannerBlue = db.Column(db.String)
    boxBlue = db.Column(db.String)

    @property 
    def banner_blue(self):
        return uploaded_photos.url(self.bannerBlue)

    @property 
    def box_blue(self):
        return uploaded_photos.url(self.boxBlue)


class Export_32(db.Model):
    __bind_key__ = "linkedin"
    __tablename__ = 'export_32'

    # id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, primary_key=True)
