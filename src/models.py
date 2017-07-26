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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<TodoList {}>".format(self.title)

    @classmethod
    def create(cls, **kwargs):
        new_data = TodoList(**kwargs)
        new_data.save()
        return new_data

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class User(UserMixin, SaveMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    email = db.Column(db.String(70))
    password = db.Column(db.String(70))
    todolists = db.relationship('TodoList', backref='user', lazy='dynamic')

    @classmethod
    def create(cls, **kwargs):
        new_user = User(**kwargs)
        new_user.save()
        return new_user

    def delete(self):
        db.session.delete(self)
        db.session.commit()
