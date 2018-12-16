from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, Length


def is_int(form, field):
    print(field.data)


class BidForm(FlaskForm):
    name = StringField(
        'name',
        validators=[
            DataRequired('Заполните имя'),
            Length(max=100, message='Поле имя не может быть больше ста букв')
        ]
    )
    phone = IntegerField(
        'phone',
        validators=[
            DataRequired('Заполните телефон'),
        ],

    )
    message = TextAreaField('message')
