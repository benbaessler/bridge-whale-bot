from dotenv import load_dotenv
import tweepy
import json
import os
# from bot import send_message

# Getting .env variables
load_dotenv() 

twitter_api_key = os.getenv('TWITTER_API_KEY')
twitter_api_secret = os.getenv('TWITTER_API_SECRET')
twitter_access_token = os.getenv('TWITTER_ACCESS_TOKEN')
twitter_access_secret = os.getenv('TWITTER_ACCESS_SECRET')
twitter_username = os.getenv('TWITTER_USERNAME')

class StreamListener(tweepy.StreamListener):

  def on_status(self, status):
    print('New Tweet from @{}'.format(twitter_username))
    tweet = status.text

    if '🦡' in tweet:
      print('New transaction on Badger Bridge')
      print(tweet)

  def on_error(self, status_code):
    print('StreamListener Error: {}'.format(status_code))
    return

if __name__ == '__main__':
  # Authorising Twitter
  auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
  auth.set_access_token(twitter_access_token, twitter_access_secret)

  api = tweepy.API(auth)

  # Streaming for incoming Tweets
  print('Streaming activities from @{}...'.format(twitter_username))
  
  user = api.get_user(twitter_username)
  stream = tweepy.Stream(auth = api.auth, listener = StreamListener())
  stream.filter(follow = [user.id_str], is_async = True)