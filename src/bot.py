import os
import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
channel = client.get_channel(os.getenv('DISCORD_CHANNEL_ID'))

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

async def send_message(tweet):
  if not client:
    return 'Discord Bot is not running'
  await client.send_message(channel, tweet['text'])

client.run(os.getenv('DISCORD_BOT_TOKEN'))