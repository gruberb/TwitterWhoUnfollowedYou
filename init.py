import api
import json

user_friends = api.api.GetFollowers()

friends = [u.name for u in user_friends];

with open('friends.txt', 'w') as json_file:
    json.dump(friends, json_file)
