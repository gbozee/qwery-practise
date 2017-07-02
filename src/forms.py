from flask_wtf import FlaskForm
from .models import TodoList
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    status = BooleanField('Status')

    def save(self):
        TodoList.create(title=self.data['title'], 
        status=self.data['status'])
    