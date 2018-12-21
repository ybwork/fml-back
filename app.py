from logging.handlers import RotatingFileHandler
import logging

from flask import Flask, render_template, request, jsonify
from flask.logging import default_handler
from flask_mail import Mail

import utils
from config import DevelopmentConfig
from forms import BidForm

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

# Logging
app.logger.removeHandler(default_handler)
file_handler = RotatingFileHandler('app.log', maxBytes=1000000, backupCount=1)
file_handler.setLevel(logging.ERROR)
app.logger.addHandler(file_handler)

# Email
mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/customers')
def customers():
    return render_template('customers.html')


@app.route('/bids', methods=['POST'])
def bids():
    return request.body


@app.route('/test', methods=['GET'])
def test():
    form = BidForm()
    return render_template('test.html', form=form)


@app.route('/ajax', methods=['POST'])
def ajax():
    form = BidForm()

    if form.validate_on_submit():
        # utils.send_mail()
        return jsonify({'message': 'Ваша заявка успешно отправлена'})

    app.logger.error('fuck')

    response = jsonify(form.errors)
    response.status_code = 400
    return response


if __name__ == '__main__':
    app.run(debug=True)
