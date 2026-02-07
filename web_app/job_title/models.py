from web_app import db


class JOB_TITLE(db.Model):
    __tablename__ = 'JOB_TITLE'
    job_title_code = db.Column(db.Integer, primary_key=True)
    job_title_name = db.Column(db.String(50))
    department_code = db.Column(db.Integer)
