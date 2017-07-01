"""This module contains all the routes"""

from flask import render_template
from app import app
from models import Team, User

@app.route("/")
def home():
    """display root route"""
    return render_template("home.html")

@app.route("/users")
def users():
    """display list of users"""
    all_users = User.find_all()
    return render_template("users.html", users=all_users)

@app.route("/users/<int:user_id>")
def user(user_id):
    """display one user"""
    # return all users whose id matches url user_id
    target_user = User.find_one(user_id)
    return render_template('user.html', user=target_user)

@app.route("/teams")
def teams():
    """display list of teams"""
    all_teams = Team.find_all()
    return render_template("teams.html", teams=all_teams)
