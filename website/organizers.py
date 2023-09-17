#codes related to organizers
from flask import Blueprint, render_template, redirect, url_for, request
from datetime import datetime
from . import db
from .models import Event, User
from sqlalchemy import select
from flask_login import login_required, current_user

organizers = Blueprint("organizers", __name__)


@organizers.route("/", methods=['GET', 'POST'])
@organizers.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        host_name = request.form.get("eventTitle")
        start_date = request.form.get("date")
        duration = request.form.get("durationHours")
        vol_need = request.form.get("volunteerNumber")
        description = request.form.get("description")
        pic_url = request.form.get("")

        user_id = current_user.id

        if host_name and start_date and duration and vol_need and description:
            new_event = Event(user_id=user_id, host_name=host_name, start_date=start_date, duration=duration, vol_need=vol_need, description=description)
            db.session.add(new_event)
            db.session.commit()
            return redirect(url_for('organizers.home'))

    return render_template('organizers.html')