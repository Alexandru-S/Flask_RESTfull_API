from web_app import db_creds

SQLALCHEMY_DATABASE_URI = ('oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{sid}').format(username=USERNAME, password=PASSWORD, hostname=HOSTNAME, port=PORT, sid=SID)