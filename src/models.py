from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SaveMixin(object):
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

class TodoList(SaveMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    status = db.Column(db.Boolean)