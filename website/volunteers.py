#codes related to organizers
from flask import Blueprint, render_template, redirect, url_for

volunteers = Blueprint("volunteers", __name__)

@volunteers.route("/")
@volunteers.route("/home") #TODO: Change below
def home():
    return render_template("home.html")