#codes related to organizers
from flask import Blueprint, render_template, redirect, url_for, request
from datetime import datetime
from . import db
from .models import Event, User
from sqlalchemy import select
from flask_login import login_required, current_user

organizers = Blueprint("organizers", __name__)


@organizers.route("/")
@organizers.route("/home") #TODO: Change below
def home():
    if request.method == 'POST':
        host_name = request.form.get("eventTitle")
        start_date = request.form.get("date")
        duration = request.form.get("durationHours")
        vol_need = request.form.get("volunteerNumber")
        description = request.form.get("description")

        start_date = start_date
        print("s", host_name)
        # event_name_exists = Event.query.filter_by(host_name=host_name)
        # user1 = User.query.filter_by(host_name==User.name).first() 
        # stmt = select(User).where(User.name==current_user)
        # print('u', stmt)
        # if event_name and start_date and duration and vol_need and description and not event_name_exists:
        #     new_event = Event(host_name=host_name, start_date=start_date, duration=duration, vol_need=vol_need, description=description)
        #     db.session.add(new_event)
        #     db.session.commit()
        #     return redirect(url_for('organizers.home'))


    return render_template('organizers.html')