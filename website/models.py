#DB tables
from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), nullable=False)
    credit_hours = db.Column(db.Integer, nullable=True)
    total_hours = db.Column(db.Integer, nullable=True)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    host_name = db.Column(db.String(150), nullable=False)
    start_date = db.Column(db.DateTime(timezone=True), nullable=False)
    end_date = db.Column(db.DateTime(timezone=True), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    credits_need = db.Column(db.Integer, nullable=False)


class Prize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"), nullable=False)
    hours_need = db.Column(db.Integer, nullable=True)


class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"), nullable=False)
    hours_worked = db.Column(db.Integer, nullable=False)