import data.app_data as data
from app import db

class Team(db.Model):
    # class properites are used to generate table fields
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # class constructor
    def __init__(self, name):
        self.name = name

    @classmethod
    def find_all_with_users(cls):
        def get_team_members(team):
            # find users whose team_id matches the given team
            team_members = filter(lambda user: user['team_id'] == team['id'], data.users())
            # add users to team
            team['users'] = list(team_members)
            return team

        # add team members to every team
        teams_with_users = list(map(get_team_members, data.teams()))
        return teams_with_users

class User(db.Model):
    # class properites are used to generate table fields
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    # class constructor
    def __init__(self, name, team_id):
        self.name = name
        self.team_id = team_id

    @classmethod
    def find_all(cls):
        return data.users()

    @classmethod
    def find_one(cls, user_id):
        return [user for user in data.users() if user['id'] == user_id][0]
