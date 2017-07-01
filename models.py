import data.app_data as data

class Team():
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

class User():
    @classmethod
    def find_all(cls):
        return data.users()

    @classmethod
    def find_one(cls, user_id):
        return [user for user in data.users() if user['id'] == user_id][0]
