from app import db
from sqlalchemy.sql import text

class Team(db.Model):
    # class properites are used to generate table fields
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    users = db.relationship('User', backref='team', lazy='dynamic')

    # class constructor
    def __init__(self, name):
        self.name = name

    @classmethod
    def find_all(cls):
        return Team.query.all()

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
        return User.query.all()

    @classmethod
    def find_one(cls, user_id):
        return User.query.filter_by(id=user_id).first()
