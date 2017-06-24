from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    status = db.Column(db.Boolean)