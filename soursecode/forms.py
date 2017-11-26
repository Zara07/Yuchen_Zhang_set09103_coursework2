from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, validators

def CheckNameLength(form, field):
  if len(field.data) < 1:
    raise ValidationError('Name must have more then 1 characters')

class ContactForm(Form):
    name = StringField('Your Name:', [validators.DataRequired(), CheckNameLength])
    email = StringField('E-mail address:', [validators.DataRequired(), validators.Email('your@email.com')])
    message = TextAreaField('Your message:', [validators.DataRequired()])
    submit = SubmitField('Submit')


