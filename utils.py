from flask import current_app as app
from logging.handlers import RotatingFileHandler

import logging

from flask.logging import default_handler
from flask_mail import Mail, Message


def write_log(message):
    app.logger.removeHandler(default_handler)
    file_handler = RotatingFileHandler('app.log', maxBytes=1000000, backupCount=1)
    file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(file_handler)
    app.logger.error(message)


def send_mail():
    # mail = Mail()
    # mail.init_app(app)
    # msg = Message('Hello', recipients=['to@example.com'])
    # msg.body = 'testing'
    # msg.html = '<b>testing</b>'
    # return mail.send(msg)
    pass
