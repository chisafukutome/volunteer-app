#codes related to authentication
from flask import Blueprint, render_template, redirect, url_for, request
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get user input
        email = request.form.get("email")
        password = request.form.get("password")

        # get user
        user = User.query.filter_by(email=email).first()
        # if user exists
        if user:
        #     check if the password is correct
            if check_password_hash(user.password, password):
                # login
                login_user(user, remember=True)
            return redirect(url_for('volunteers.home'))
    return render_template("login.html")

@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get user input
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if email already exists
        email_exists = User.query.filter_by(email=email).first()
        if not email_exists:
            # Add the user data into the db
            new_user = User(name=name, email=email, password=generate_password_hash(password, method='pbkdf2'))
            db.session.add(new_user)
            db.session.commit()

            # login user
            login_user(new_user, remember=True)

            return redirect(url_for('volunteers.home'))
    return render_template("signup.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))