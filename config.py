import os


class DevelopmentConfig():
    SECRET_KEY = os.urandom(16)


class ProductionConfig():
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'you'
    MAIL_PASSWORD = 'your-password'
