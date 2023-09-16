# DB tables
from . import db


class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String, nullable=False)
    credit_hours = db.Column(db.Integer, nullable=False)
    total_hours = db.Column(db.Integer, nullable=False)


class Event(db.model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    host_name = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    vol_need = db.Column(db.Integer, nullable=False)


class Sponsor(db.model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    hour_need = db.Column(db.Integer, nullable=True)


class Volunteering(db.model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    e_id = db.Column(db.Integer, db.ForeignKey("Event.id"), nullable=False)
    hours_worked = db.Column(db.Integer, nullable=False)

