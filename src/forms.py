from builtins import super
from flask import flash
from flask_wtf import FlaskForm
from .models import TodoList, User
from wtforms import StringField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.widgets import TextArea, PasswordInput
from flask_login import login_user


class TodoForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    status = SelectField('Status', choices=[('U', 'Undone'), ('D', 'Done')])

    def save(self):
        TodoList.create(title=self.data['title'],
                        status=(True if self.data['status'] == 'D' else False))


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField(
        "Password", widget=PasswordInput(), validators=[DataRequired()])

    def validate(self):
        result = super().validate()
        email = self.data['email']
        password = self.data['password']
        user = self.get_user()
        if user and password == user.password:
            return True
        flash('Invalid email/password combination', 'danger')
        return False

    def get_user(self):
        return User.query.filter(User.email == self.data['email']).first()


class SignupForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField('Email', validators=[
        DataRequired(),
        Email(message='Please enter a valid email address')
    ])
    password = PasswordField('Choose a Password', validators=[
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password', validators=[DataRequired()])

    def validate(self):
        result = super().validate()
        email = self.data['email']
        user = self.get_user("email")
        if user:
            flash('Email is already in use', 'danger')
            return False
        user = self.get_user("username")
        if user:
            flash('Username already taken', 'danger')
            return False
        return True

    def get_user(self, param):
        if param == "email":
            return User.query.filter(User.email == self.data['email']).first()
        if param == "username":
            return User.query.filter(User.username == self.data['username']).first()

    def save(self):
        User.create(username=self.data['username'],
                    email=self.data['email'], password=self.data['password'])
