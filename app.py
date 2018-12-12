from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import IntegerField
from wtforms import TextAreaField
from wtforms.validators import DataRequired

from flask_wtf.csrf import CSRFProtect
import os

class BidForm(FlaskForm):
	name = StringField('name', validators=[DataRequired('поле должно быть')])
	phone = IntegerField('phone', validators=[DataRequired('поле должно быть')])
	message = TextAreaField('message')

app = Flask(__name__)
app.secret_key = os.urandom(16)

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
		return jsonify({'message': 'Ваша заявка успешно отправлена'})
		
	response = jsonify({'message': 'Заполните имя и телефон'})
	response.status_code = 400
	return response

if __name__ == '__main__':
	app.run(debug=True)