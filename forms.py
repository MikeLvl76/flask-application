from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class Form(FlaskForm):
    message = StringField(
        'Message',
        [DataRequired()]
    )
    types = SelectField(
        u'Types', 
        choices=[
            ('ascii', 'Ascii'), ('digit', 'Digit'), ('emoji', 'Emoji')
        ]
    )
    submit = SubmitField('Submit')