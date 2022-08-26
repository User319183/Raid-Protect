import discord

from discord.ext import commands

from discord import activity

from discord.commands import Option

import os
import sys

import json

import asyncio as asyncio

import re
import string


from discord.ext import *
from discord.ext.commands import *
from ctypes import *
import datetime

from discord import Message

import aiohttp

from pymongo import MongoClient

from discord import option


class AntiSpam(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    
    


# let's work on anti-spam later. We need to work on how we will do the on_message event.


    # @commands.slash_command()
    # @commands.has_permissions(administrator=True)
    # async def antispam(self, ctx, option: Option(str, "Should we enable or disable antispam mode?", choices=["Enable", "Disable"])):
        
        # client = MongoClient("mongodb+srv://User:PASSWORD@cluster0.fdd0q.mongodb.net/DB_NAME?retryWrites=true&w=majority")
        # db = client.THEDATABASE
        # collection = db.antispam
        


    #     if option == "Enable":

    #         collection.replace_one({"guild_id": ctx.guild.id}, {"guild_id": ctx.guild.id, "option": "Enable"}, upsert=True)

    #         await ctx.respond(f"Anti-Spam has been enabled for `{ctx.guild.name}`.")

    #     elif option == "Disable":
    #         collection.replace_one({"guild_id": ctx.guild.id}, {"guild_id": ctx.guild.id, "option": "Disable"}, upsert=True)
    #         await ctx.respond(f"Anti-Spam has been disabled for `{ctx.guild.name}`.")
            
            
            
            

            
            
def setup(bot):
	bot.add_cog(AntiSpam(bot))
