



import discord

from discord.ext import commands

import os

import json

import asyncio as asyncio

from discord.ext import *

from discord.ext.commands import *

from ctypes import *

from pymongo import MongoClient

from discord import option

import re



if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

token = configData["Token"]








intents = discord.Intents.default()
intents.message_content = True
# intents.typing = False
# intents.presences = False
intents.members = True
intents.reactions = True



bot = commands.Bot(command_prefix="ar-", intents=intents, activity=discord.Activity(type=discord.ActivityType.watching, name=f"for raids"))

bot.remove_command('help')

for fn in os.listdir('./cogs'):
	if fn.endswith('.py'):
		bot.load_extension(f"cogs.{fn[:-3]}")
  
  
  
  
#### Source code protected by the GNU GENERAL PUBLIC LICENSE Version 3.


# </help:COMMAND_ID> TO MENTION A COMMAND IN THE BOT!!




@bot.listen()
async def on_ready():
    print(f'Bot has been activated! Modules loaded. Source code protected by the GNU GENERAL PUBLIC LICENSE Version 3.')
    print(f'---------------------------------------')
    





bot.run(token)
