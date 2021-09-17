from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    email = StringField('Enter Your Email Address Here...',validators=[Required(),Email()])
    username = StringField('Enter Your Username Here...',validators = [Required()])
    password = PasswordField('Enter Password Here...',validators = [Required(),EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Re-enter Password Here For Confirmation',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('Sorry the email you have entered has already been registered, if it was yours then your are cleared to login.')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email= StringField('Enter Your Email Address Here...' ,validators =[Required(),Email()])
    password = PasswordField('Enter Password Here', validators = [Required()])
    remember =  BooleanField('Remember me')
    submit = SubmitField('Login')
