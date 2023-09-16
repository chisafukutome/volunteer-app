#codes related to organizers
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

volunteers = Blueprint("volunteers", __name__)

@volunteers.route("/")
@volunteers.route("/home") #TODO: Change below
@login_required
def home():
    return render_template("test.html", name=current_user.name)