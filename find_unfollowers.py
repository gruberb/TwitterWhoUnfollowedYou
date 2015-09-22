import api
import json

user_friends = api.api.GetFollowers()

friends = [u.name for u in user_friends];

with open('friends_temp.txt', 'w') as json_file:
    json.dump(friends, json_file)

ft = open("friends_temp.txt", "r")
friends_temp = ft.read().replace('[', '').replace(']', '').split(',')

f = open("friends.txt", "r")
last_friends = f.read().replace('[', '').replace(']', '').split(',')

if friends_temp == last_friends:
    print "Nothing changed"
else:
    for friend in last_friends:
        if friend not in friends_temp:
            print friend + " is not your friend anymore :("
