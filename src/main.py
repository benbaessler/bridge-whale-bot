from dotenv import load_dotenv
import discord
import tweepy
import json
import os

# Getting .env variables
load_dotenv() 

twitter_api_key = os.getenv('TWITTER_API_KEY')
twitter_api_secret = os.getenv('TWITTER_API_SECRET')
twitter_access_token = os.getenv('TWITTER_ACCESS_TOKEN')
twitter_access_secret = os.getenv('TWITTER_ACCESS_SECRET')
twitter_username = os.getenv('TWITTER_USERNAME')

discord_channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))
discord_bot_token = os.getenv('DISCORD_BOT_TOKEN')

client = discord.Client()

class StreamListener(tweepy.StreamListener):

  def on_status(self, status):
    print('New Tweet from @{}'.format(twitter_username))
    tweet = status.text

    if '🦡' in tweet:
      print('New transaction on Badger Bridge')
      send_message(tweet)

  def on_error(self, status_code):
    print('StreamListener Error: {}'.format(status_code))
    return

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user: return

  # Testing
  if message.channel.id == discord_channel_id:
    await message.channel.send('Hey {}'.format(message.author.name))

def send_message(message):
  channel = client.get_channel(discord_channel_id)
  action = channel.send(message)
  client.loop.create_task(action)

# Authorising Twitter
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
auth.set_access_token(twitter_access_token, twitter_access_secret)

api = tweepy.API(auth)

# Streaming for incoming Tweets

user = api.get_user(twitter_username)
stream = tweepy.Stream(auth, StreamListener())

try:
  print('Streaming activities from @{}...'.format(twitter_username))
  stream.filter(follow = [user.id_str], is_async = True)
  client.run(discord_bot_token)

finally:
  print('Ending process...')
  client.close()

