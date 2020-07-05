import os

# Configure SQL, JWT and Mailtrap
class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_SQLALCHEMY_DATABASE_URI')
    # or use
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLITE_SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '23edf956eed858'
    MAIL_PASSWORD = '4eef1094a3b044'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    