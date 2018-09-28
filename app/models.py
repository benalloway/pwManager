from app import db, login
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# For flask-login to handle loading a user
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#######################
# User Model
#######################
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    group_id = db.Column(db.Integer, db.ForeignKey('group.id')) # not sure if needed.

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

#######################
# Group Model
#######################
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean())
    users = db.relationship('User', backref='group', lazy='dynamic')

    def __repr__(self):
        return '<Group {}>'.format(self.group_name)    