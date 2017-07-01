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
    def find_all(cls):
        teams = data.teams()
        users = data.users()

        def get_team_members(team):
            # find users whose team_id matches the given team
            team_members = [user for user in users if user['team_id'] == team['id']]

            # add users to team
            return {'name': team['name'], 'id': team['id'], 'users': team_members}

        return [get_team_members(team) for team in teams]

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
