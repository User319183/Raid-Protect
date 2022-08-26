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



class Autokick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    
    
    
    
    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def autokick(self, ctx, option: Option(str, "Should we enable or disable auto kick mode?", choices=["Enable", "Disable"])):
        
        client = MongoClient("mongodb+srv://User:PASSWORD@cluster0.fdd0q.mongodb.net/DB_NAME?retryWrites=true&w=majority")
        db = client.THEDATABASE
        collection = db.autokick
        


        if option == "Enable":

            collection.replace_one({"guild_id": ctx.guild.id}, {"guild_id": ctx.guild.id, "option": "Enable"}, upsert=True)

            await ctx.respond(f"Auto kick mode has been enabled for `{ctx.guild.name}`. New members will be kicked.")

        elif option == "Disable":
            collection.replace_one({"guild_id": ctx.guild.id}, {"guild_id": ctx.guild.id, "option": "Disable"}, upsert=True)
            await ctx.respond(f"Auto kick mode has been disabled for `{ctx.guild.name}` New members will no longer be kicked.")
                
                
    


    @commands.Cog.listener()
    async def on_member_join(self, member):

        client = MongoClient("mongodb+srv://User:PASSWORD@cluster0.fdd0q.mongodb.net/DB_NAME?retryWrites=true&w=majority")
        db = client.THEDATABASE
        collection = db.autokick
        
        if member.bot:
            return
        
        #if the collection is not empty or disabled
        if collection.count_documents({"guild_id": member.guild.id}) > 0:
            if collection.find_one({"guild_id": member.guild.id})["option"] == "Enable":
        

                await member.send("This server is protected by the module **auto-kick**. New users are not allowed to join this server.")
                await member.kick()
  
  
  
def setup(bot):
	bot.add_cog(Autokick(bot))
