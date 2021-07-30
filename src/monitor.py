import os
import json
import tweepy
from bot import send_message
from dotenv import load_dotenv

load_dotenv() 

# Authorising Twitter
auth = tweepy.OAuthHandler(os.getenv('TWITTER_API_KEY'), os.getenv('TWITTER_API_SECRET'))
auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_SECRET'))

api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):

  def on_data(self, data):
    print('Something happened!')
    tweet = json.loads(data)

    valid = filter(tweet)
    if valid:
      print('New transaction on Badger Bridge')
      # print(tweet['text'])

      send_message(tweet)

  def on_status(self, status):
    print(status.text)

def start():
  user = api.get_user(os.getenv('TWITTER_USERNAME'))

  # Streaming for new tweets
  print('Streaming activities from @{}...'.format(os.getenv('TWITTER_USERNAME')))
  stream_listener = StreamListener()
  stream = tweepy.Stream(auth = api.auth, listener = stream_listener)
  stream.filter(follow=[user.id_str])

def filter(tweet):
  if (tweet['text'][0] == '🦡'):
    return True
  return False