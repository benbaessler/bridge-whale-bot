import os
import tweepy
from dotenv import load_dotenv

load_dotenv() 

auth = tweepy.OAuthHandler(os.getenv('TWITTER_API_KEY'), os.getenv('TWITTER_API_SECRET'))
auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_SECRET'))

api = tweepy.API(auth)

class Monitor:

  def start():
    user = api.get_user(os.getenv('TWITTER_USERNAME'))
    print(user.followers_count)
