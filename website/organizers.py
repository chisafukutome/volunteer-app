#codes related to organizers
from flask import Blueprint, render_template, redirect, url_for, request
from datetime import datetime
from flask_login import login_required, current_user

organizers = Blueprint("organizers", __name__)

@organizers.route("/", methods=['GET', 'POST'])
@organizers.route("/home", methods=['GET', 'POST'])
@login_required
def organiser():
    if request.method == 'POST':
        event_name = request.form.get("eventTitle")
        start_date = request.form.get("date")
        start_Time = request.form.get("time")
        duration = request.form.get("durationHours")
        vol_need = request.form.get("volunteerNumber")
        description = request.form.get("description")

        start_date = start_date+start_Time
        print("s", start_date)
        start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
        print(start_date)

    return render_template('dashboard-old.html')