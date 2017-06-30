from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class TodoForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    status = SelectField('Status', choices=[('U', 'Undone'), ('D','Done')])