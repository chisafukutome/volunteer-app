#codes related to pages before authentication
from flask import Blueprint, render_template, redirect, url_for
from .models import Event, Prize

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    # Select all of events & prizes
    events = Event.query.all() #TODO: Filter by date
    prizes = Prize.query.filter(Prize.quantity > 0)
    return render_template("home.html", events=events, prizes=prizes)

