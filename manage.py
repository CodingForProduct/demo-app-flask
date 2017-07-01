import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from models import *

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def seed():
    # delete all records in database
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print ('Clear table %s' % table)
        db.session.execute(table.delete())
    db.session.commit()

    print("Seeding teams...")
    # create new team objects
    team1 = Team('Team One')
    team2 = Team('Team Two')
    # begins talking to the database
    db.session.add_all([team1, team2])
    # save teams database
    db.session.commit()

    print("Seeding users...")
    # create new user objects
    user1 = User('Emily', team1.id)
    user2 = User('Madison', team2.id)
    user3 = User('Emma', team2.id)
    user4 = User('Hannah', team1.id)
    user5 = User('Olivia', team2.id)
    # begins talking to the database
    db.session.add_all([user1, user2, user3, user4, user5])
    # save users database
    db.session.commit()

    print("Done seeding")

if __name__ == '__main__':
    manager.run()
