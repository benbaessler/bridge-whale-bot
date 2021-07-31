import os
import json
import tweepy
# from bot import send_message
from dotenv import load_dotenv

load_dotenv() 

# Getting .env variables
twitter_api_key = os.getenv('TWITTER_API_KEY')
twitter_api_secret = os.getenv('TWITTER_API_SECRET')
twitter_access_token = os.getenv('TWITTER_ACCESS_TOKEN')
twitter_access_secret = os.getenv('TWITTER_ACCESS_SECRET')
twitter_username = os.getenv('TWITTER_USERNAME')

# Authorising Twitter
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
auth.set_access_token(twitter_access_token, twitter_access_secret)

api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):

  def on_data(self, data):
    print('New Tweet from @{}'.format(twitter_username))
    tweet = json.loads(data)

    valid = filter(tweet)
    if valid:
      print('New transaction on Badger Bridge')
      print(tweet['text'])

      # send_message(tweet)

  def on_status(self, status):
    print(status.text)

  def on_error(self, status_code):
    if status_code == 420:
      print(False)

def start():
  user = api.get_user(twitter_username)

  # Streaming for new tweets
  print('Streaming activities from @{}...'.format(twitter_username))
  stream_listener = StreamListener()
  stream = tweepy.Stream(auth = api.auth, listener = stream_listener)
  stream.filter(follow=[user.id_str], is_async = True)

def filter(tweet):
  if (tweet['text'][0] == '🦡') :
    return True
  return False