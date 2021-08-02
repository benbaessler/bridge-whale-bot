from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import load_dotenv
from datetime import datetime
import tweepy
import time
import os

# Getting .env variables
load_dotenv() 

twitter_username = os.getenv('TWITTER_USERNAME')
twitter_api_key = os.getenv('TWITTER_API_KEY')
twitter_api_secret = os.getenv('TWITTER_API_SECRET')
twitter_access_token = os.getenv('TWITTER_ACCESS_TOKEN')
twitter_access_secret = os.getenv('TWITTER_ACCESS_SECRET')
discord_webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

webhook = DiscordWebhook(discord_webhook_url)

class StreamListener(tweepy.StreamListener):

  def on_status(self, status):
    print('({}) New Tweet from @{}'.format(get_timestamp(), twitter_username))

    if '🦡' in status.text:
      print('({}) New transaction on Badger Bridge'.format(get_timestamp()))
      send_webhook(status)

  def on_error(self, status_code):
    print('({}) StreamListener Error: {}'.format(get_timestamp(), status_code))
    return

def get_timestamp():
  time_obj = datetime.now()
  return time_obj.strftime('%H:%M:%S')

def send_webhook(tweet):
  message_embed = DiscordEmbed(
    title = '{} (@{})'.format(user.name, user.screen_name),
    url = 'https://twitter.com/{}/status/{}'.format(twitter_username, tweet.id_str),
    description = tweet.text,
    color = 0xf2a52b
  )
  webhook.add_embed(message_embed)
  response = webhook.execute()


# Authorising Twitter
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
auth.set_access_token(twitter_access_token, twitter_access_secret)

api = tweepy.API(auth)

user = api.get_user(twitter_username)
stream = tweepy.Stream(auth, StreamListener())

print('({}) Streaming activities from @{}...'.format(get_timestamp(), twitter_username))

while True:
  try:
    stream.filter(follow = [user.id_str], is_async = True)
  except:
    continue

