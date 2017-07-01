from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

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

    def __repr__(self):
        return "<TodoList {}>".format(self.title)

    @classmethod
    def create(cls,**kwargs):
        new_data = TodoList(**kwargs)
        new_data.save()
        return new_data

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(70))
    username = db.Column(db.String())
