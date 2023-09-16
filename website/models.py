# DB tables
from . import db


class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String, nullable=False)


class Event(db.model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    host_name = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    hours = db.Column(db.Integer, nullable=False)


class Sponsor(db.model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    e_id = db.Column(db.Integer, db.ForeignKey("Event.id"), nullable=False)


class Volunteering(db.model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    e_id = db.Column(db.Integer, db.ForeignKey("Event.id"), nullable=False)
    hours_worked = db.Column(db.Integer, nullable=False)
