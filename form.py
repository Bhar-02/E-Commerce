from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from app.models import User
from app import app 

class Signup(FlaskForm):

    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)]) 
    email=StringField('Email',validators=[DataRequired(),Email()]) 
    password=PasswordField('Password',validators=[DataRequired(),Length(min=8)])
    confirmpassword=PasswordField('ConfirmPassword',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign up') 
    
    def validate_username(self, username):
        with app.app_context():
            user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken. Please choose a different one.')

    def validate_email(self, email):
        with app.app_context():
            user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken. Please choose a different one.')



class Login(FlaskForm):

    email=StringField('Email',validators=[DataRequired(),Email()]) 
    password=PasswordField('Password',validators=[DataRequired(),Length(min=8)])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Log in')



class StoreForm(FlaskForm):

    Category=StringField ('Category',validators=[DataRequired()]) 
    Product=StringField('Product',validators=[DataRequired()])
    Amount=StringField('Integer',validators=[DataRequired()])
    submit=SubmitField('Update')
  
