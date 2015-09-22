import twitter
import credentials

api = twitter.Api(consumer_key=credentials.twitter['consumer_key'],
                  consumer_secret=credentials.twitter['consumer_secret'],
                  access_token_key=credentials.twitter['access_token_key'],
                  access_token_secret=credentials.twitter['access_token_secret'])
