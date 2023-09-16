#codes related to organizers
from flask import Blueprint, render_template, redirect, url_for

organizers = Blueprint("organizers", __name__)

@organizers.route("/")
@organizers.route("/home") #TODO: Change below
def home():
    return render_template("org-dashboard.html")