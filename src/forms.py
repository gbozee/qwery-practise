from flask_wtf import FlaskForm
from .models import TodoList, User
from wtforms import StringField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.widgets import TextArea, PasswordInput
from flask_login import login_user

class TodoForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    status = SelectField('Status', choices=[('U', 'Undone'), ('D','Done')])

    def save(self):
        TodoList.create(title=self.data['title'], 
        status=(True if self.data['status'] == 'D' else False))

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password", widget=PasswordInput(), validators=[DataRequired()])

    def validate(self):
        # result = super().validate()
        email = self.data['email']
        password = self.data['password']
        if email and password:
            if email == "yemisi@gmail.com" and password == "password":
                return True
            self.email.errors.append('Invalid email/password combination')
        return False

    def get_user(self):
        return User()


class SignupForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Choose a Password', validators=[DataRequired()])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
