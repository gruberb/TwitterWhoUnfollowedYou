import twitter
import credentials
import json

api = twitter.Api(consumer_key=credentials.twitter['consumer_key'],
                  consumer_secret=credentials.twitter['consumer_secret'],
                  access_token_key=credentials.twitter['access_token_key'],
                  access_token_secret=credentials.twitter['access_token_secret'])

user_friends = api.GetFriends()
print(user_friends)

with open('user_friends.txt', 'w') as json_file:
    json.dump(user_friends, json_file)