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


class AntiInvites(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    
    
    
    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def invite_mode(self, ctx, option: Option(str, "Should we enable or disable invite mode?", choices=["Enable", "Disable"])):
        
        client = MongoClient("mongodb+srv://User:PASSWORD@cluster0.fdd0q.mongodb.net/DB_NAME?retryWrites=true&w=majority")
        db = client.THEDATABASE
        collection = db.antiinvites
        


        if option == "Enable":

            collection.replace_one({"guild_id": ctx.guild.id}, {"guild_id": ctx.guild.id, "option": "Enable"}, upsert=True)

            await ctx.respond(f"Invite mode has been enabled for `{ctx.guild.name}`.")

        elif option == "Disable":
            collection.replace_one({"guild_id": ctx.guild.id}, {"guild_id": ctx.guild.id, "option": "Disable"}, upsert=True)
            await ctx.respond(f"Invite mode has been disabled for `{ctx.guild.name}`.")
                
                
                








    @commands.Cog.listener()
    async def on_message(self, message: Message):
            
        client = MongoClient("mongodb+srv://User:PASSWORD@cluster0.fdd0q.mongodb.net/DB_NAME?retryWrites=true&w=majority")
        db = client.THEDATABASE
        collection = db.antiinvites


        #if message author is a bot
        if message.author.bot:
            return

        else:
            
            #if the guild_id is in the database, let's see if the option is enabled
            
            try:
                    
                if collection.find_one({"guild_id": message.guild.id})["option"] == "Enable":
                    #if the message contains a discord invite link, delete it. Discord invite links are discord.gg/ and random letters
                    if re.search(r"discord.gg/\w+", message.content):
                        await message.delete()
                        await message.channel.send(f"{message.author.mention} Invite links are not allowed in this server.")
                        return
                    else:
                        return
                    
            except:
                pass
                

        

  
  
def setup(bot):
	bot.add_cog(AntiInvites(bot))
