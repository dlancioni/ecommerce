from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired, ValidationError, email_validator

# Custom validator to be used in any below class (must have sub function)
def length(min=-1, max=-1, message=""):
    message = message % (min, max)
    def _length(self, field):
        l = field.data and len(field.data) or 0
        if l < min or max != -1 and l > max:
            raise ValidationError(message)
    return _length

class FormStore(FlaskForm):
    searchbar = StringField(label=(""), validators=[length(min=5, max=50, message="Pesquisa deve ter entre %d e %d caracteres")])