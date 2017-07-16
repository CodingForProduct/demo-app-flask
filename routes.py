"""This module contains all the routes"""

from flask import render_template, request,redirect,url_for
from app import app, db
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


def isValid(formData):
    if (formData['name'].strip() != ''):
        return True
    else:
        return False

@app.route('/teams', methods=['POST'])
def create_team():
    name = request.form['name']
    if isValid(request.form):
        team = Team(name)
        # save team to database
        db.session.add(team)
        db.session.commit()
        # redirect to home page
        return redirect(url_for('teams'))
    else:
        return redirect(url_for('new_team'))

@app.route('/teams/new')
def new_team():
    return render_template("teamsNew.html")

@app.route("/teams/<int:team_id>")
def show_team(team_id):
    target_team = Team.query.filter_by(id=team_id).first()
    return render_template('team.html', team=target_team)

@app.route("/teams/<int:team_id>/delete", methods=['POST'])
def delete_team(team_id):
    team = Team.query.filter_by(id=team_id).first()
    db.session.delete(team)
    db.session.commit()
    return redirect(url_for('teams'))

@app.route("/teams/<int:team_id>/edit")
def show_edit_team(team_id):
    team = Team.query.filter_by(id=team_id).first()
    return render_template('teamsEdit.html', team=team)


@app.route("/teams/<int:team_id>/edit", methods=['POST'])
def edit_team(team_id):
    name = request.form['name']

    team = Team.query.filter_by(id=team_id).first()
    setattr(team, 'name', name)
    db.session.commit()
    return redirect(url_for('show_team', team_id=team_id))
