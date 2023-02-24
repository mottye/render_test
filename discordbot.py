import discord
import requests
import json
import re
from discord import Intents, Client, Interaction, Member, ButtonStyle, ui, app_commands
import os

# -------------------------------------- #
#                メイン処理                #
# -------------------------------------- #
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# ------------------------- #
#       Bot起動時の処理       #
# ------------------------- #
@client.event
async def on_ready():
  print("botが起動しました")

@client.event
async def on_message(message):
  if message.author.bot  : return
  channel = client.get_channel(message.channel.id)
  await channel.send("メッセージを受信しました")

# ------------------------- #
#          botの実行         #
# ------------------------- #
client.run(os.getenv('TOKEN'))