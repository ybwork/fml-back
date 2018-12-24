from logging.handlers import RotatingFileHandler

import logging

from flask.logging import default_handler
from flask_mail import Mail

from app import App

app = App.get_app()


def write_log(message):
    app.logger.removeHandler(default_handler)
    file_handler = RotatingFileHandler('app.log', maxBytes=1000000, backupCount=1)
    file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(file_handler)
    app.logger.error(message)


def send_mail():
    mail = Mail(app)
    return 'send_mail'
