from flas_wtf import FlaskForm
from wtfforms import StrinField, PasswordField, BooleanField, SubmitField
from wtfforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password'. validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
