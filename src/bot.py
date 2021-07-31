import os
import discord
from dotenv import load_dotenv

load_dotenv()

discord_channel_id = os.getenv('DISCORD_CHANNEL_ID')
discord_bot_token = os.getenv('DISCORD_BOT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user: return

  if str(message.channel.id) == discord_channel_id:
    await message.channel.send('Hey {}'.format(message.author.name))

client.run(discord_bot_token)