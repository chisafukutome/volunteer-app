#codes related to sponsors
from flask import Blueprint, render_template, redirect, url_for

sponsors = Blueprint("sponsors", __name__)

@sponsors.route("/")
@sponsors.route("/home") #TODO: Change below
def home():
    return render_template("home.html")
    return render_template("home.html")