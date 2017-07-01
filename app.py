"""This module runs the Flask app"""

# libraries that this app needs
from flask import Flask, render_template
import data.app_data as data

# initialize app
# __name__ helps determine root path
app = Flask(__name__)

# turn on debug to automatically restart app when changes are made
app.debug = True

@app.route("/")
def home():
    """display root route"""
    return render_template("home.html")

# array of users
WORKSHOP_USERS = data.users()
# array of teams
WORKSHOP_TEAMS = data.teams()

@app.route("/users")
def users():
    """display list of users"""
    return render_template("users.html", users=WORKSHOP_USERS)

@app.route("/users/<int:user_id>")
def user(user_id):
    """display one user"""
    # return all users whose id matches url user_id
    target_user = [user for user in WORKSHOP_USERS if user['id'] == user_id]

    return render_template('user.html', user=target_user[0])

@app.route("/teams")
def teams():
    """display list of teams"""
    def get_team_members(team):
        # find users whose team_id matches the given team
        team_members = filter(lambda user: user['team_id'] == team['id'], WORKSHOP_USERS)
        # add users to team
        team['users'] = list(team_members)
        return team

    # add team members to every team
    teams_with_users = list(map(get_team_members, WORKSHOP_TEAMS))
    return render_template("teams.html", teams=teams_with_users)


# only start web server if app.py is called directly;
# when file is called directly, __name__  is "__main__"
if __name__ == "__main__":
    # start server
    app.run()
