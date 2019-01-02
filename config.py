import os


class Config():
    SECRET_KEY = os.urandom(16)


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    # MAIL_DEFAULT_SENDER = 'kaduk2593@gmail.com'
    MAIL_USERNAME = 'you'
    MAIL_PASSWORD = 'your-password'
