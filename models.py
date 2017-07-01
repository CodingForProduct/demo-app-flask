import data.app_data as data

class Team():
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

class User():
    @classmethod
    def find_all(cls):
        return data.users()

    @classmethod
    def find_one(cls, user_id):
        return [user for user in data.users() if user['id'] == user_id][0]
