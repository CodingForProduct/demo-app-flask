"""This module runs the Flask app"""

# libraries that this app needs
from flask import Flask, render_template
from models import Team, User

# initialize app
# __name__ helps determine root path
app = Flask(__name__)

# turn on debug to automatically restart app when changes are made
app.debug = True

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

    all_teams = Team.find_all_with_users()
    return render_template("teams.html", teams=all_teams)


# only start web server if app.py is called directly;
# when file is called directly, __name__  is "__main__"
if __name__ == "__main__":
    # start server
    app.run()
