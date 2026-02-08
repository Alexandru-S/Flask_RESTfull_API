import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()
auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

from .department import Department
from .employee import Employee
from .badge import Badge
from .job_title import JobTitle

users = {os.getenv('USERNAME'): generate_password_hash(os.getenv('PASSWORD'))}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


api.add_resource(Department, '/department')
api.add_resource(Badge, '/badges', '/badges/<string:var1>')
api.add_resource(Employee, '/employees', '/employees/<string:var1>')
api.add_resource(JobTitle, '/job_titles', '/job_titles/<string:var1>')
SQLALCHEMY_DATABASE_URI = (
    'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{database}'
).format(
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    hostname=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'))


def create_app(config_name):
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    auto_create_schema = os.getenv('AUTO_CREATE_SCHEMA', '').strip().lower()
    if auto_create_schema in {'1', 'true', 'yes'}:
        with app.app_context():
            db.create_all()
    return app
