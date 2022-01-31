



import discord

from discord.ext import commands

import os

import json

import asyncio as asyncio

from discord.ext import *

from discord.ext.commands import *

from ctypes import *






if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

token = configData["Token"]








intents = discord.Intents.default()
# intents.typing = False
# intents.presences = False
intents.members = True
intents.reactions = True



bot = commands.AutoShardedBot(command_prefix="ar-", intents=intents, activity=discord.Activity(type=discord.ActivityType.watching, name=f"for raids"))

bot.remove_command('help')

for fn in os.listdir('./cogs'):
	if fn.endswith('.py'):
		bot.load_extension(f"cogs.{fn[:-3]}")
  
  
  


@bot.listen()
async def on_ready():
    print(f'Bot has been activated! Modules loaded.')
    print(f'---------------------------------------')
    
    






@bot.listen()
async def on_ready():
    print("ready")
    while True:
        print("cleared antispam.txt")
        await asyncio.sleep(10)
        with open("cogs/spamdetect.txt", "r+") as file:
            file.truncate(0)



@bot.listen()
async def on_ready():
    with open("cogs/raidmode.txt", "r+") as file2:
        file2.truncate(0)
        file2.writelines("off") 

        
        
        
@bot.listen()
async def on_ready():
    with open("cogs/spammode.txt", "r+") as file3:
        file3.truncate(0)
        file3.writelines("off") 

            
            
@bot.listen()
async def on_ready():
    with open("cogs/toxicity.txt", "r+") as file4:
        file4.truncate(0)
        file4.writelines("off") 




@bot.listen()
async def on_ready():
    with open("cogs/autokick.txt", "r+") as file5:
        file5.truncate(0)
        file5.writelines("off") 
        
        
        

@bot.listen()
async def on_ready():
    with open("cogs/invites.txt", "r+") as file6:
        file6.truncate(0)
        file6.writelines("off") 
        
        
        
        
        
@bot.listen()
async def on_ready():
    with open("cogs/log.txt", "r+") as file7:
        file7.truncate(0)
        file7.writelines("off") 


bot.run(token)