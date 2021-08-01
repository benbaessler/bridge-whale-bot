from discord.ext import tasks, commands
from dotenv import load_dotenv
import discord
import os

load_dotenv()

discord_channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))
discord_bot_token = os.getenv('DISCORD_BOT_TOKEN')

client = commands.Bot(command_prefix = '!')
# channel = client.get_channel(discord_channel_id)

class DiscordCog(commands.Cog):

  def __init__(self, client):
    self.client = client
    self.send_onready_message.start()

  def cog_unload(self):
    self.send_onready_message.close()
    return

  @tasks.loop(count = 1)
  async def send_onready_message(self):
    channel = self.client.get_channel(int(discord_channel_id))
    await channel.send('Hello!')

  @send_onready_message.before_loop
  async def before_send(self):
    await self.client.wait_until_ready()
    return

  @send_onready_message.after_loop
  async def after_send(self):
    self.send_onready_message.close()
    return

class TaskRunner():
  def __init__(self, client):
    self.client = client

  def run_tasks(self):
    DiscordCog(self.client)
    return


@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user: return

  # Testing
  if str(message.channel.id) == discord_channel_id:
    await message.channel.send('Hey {}'.format(message.author.name))

async def background():
  await client.wait_until_ready()
  channel = client.get_channel(discord_channel_id)
  await channel.send('Hello!')

runner = TaskRunner(client)
runner.run_tasks()

client.run(discord_bot_token)