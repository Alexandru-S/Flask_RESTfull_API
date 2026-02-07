from web_app import db


class BADGE(db.Model):
    __tablename__ = 'BADGE'
    badge_number = db.Column(db.Integer, primary_key=True)
    badge_status = db.Column(db.String(10))
    badge_expiry_date = db.Column(db.Date())
