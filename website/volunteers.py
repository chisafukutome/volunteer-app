#codes related to organizers
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from .models import Event, Prize
from datetime import datetime

volunteers = Blueprint("volunteers", __name__)

@volunteers.route("/")
@volunteers.route("/home")
@login_required
def home():
    # Select all of events
    events = Event.query.all() #TODO: Filter by date
    prizes = Prize.query.filter(Prize.quantity > 0)

    # Format the date
    for event in events:
        event1 = datetime.strptime(event.start_date, "%Y-%m-%dT%H:%M")
        event.start_date = event1.strftime("%b %d, %Y")
    return render_template("volunteers.html", name=current_user.name, prizes=prizes, events=events)

