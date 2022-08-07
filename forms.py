from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class Form(FlaskForm):
    message = TextAreaField(
        'Message (500 characters max.)',
        [DataRequired()]
    )
    types = SelectField(
        u'Type', 
        choices=[
            ('lowercase', 'Lowercase'), 
            ('uppercase', 'Uppercase'), 
            ('digit', 'Digit'), 
            ('symbol1', 'Symbol 1'),
            ('symbol2', 'Symbol 2'),
            ('symbol3', 'Symbol 3'),
            ('emoji', 'Emoji')
        ]
    )
    submit = SubmitField('Submit')