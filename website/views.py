#codes related to pages before authentication
from flask import Blueprint, render_template, redirect, url_for
from .models import Event

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    # Select all of events
    events = Event.query.all()
    return render_template("home.html", events=events)

