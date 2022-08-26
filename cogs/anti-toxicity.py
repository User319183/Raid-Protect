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



class toxicity(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    
    
    
    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def antitoxicity(self, ctx, option: Option(str, "Should we enable or disable anti toxicity mode?", choices=["Enable", "Disable"])):
        
        client = MongoClient("mongodb+srv://User:PASSWORD@cluster0.fdd0q.mongodb.net/DB_NAME?retryWrites=true&w=majority")
        db = client.THEDATABASE
        collection = db.antitoxicity
        


        if option == "Enable":

            collection.replace_one({"guild_id": ctx.guild.id}, {"guild_id": ctx.guild.id, "option": "Enable"}, upsert=True)

            await ctx.respond(f"Anti toxicity has been enabled for `{ctx.guild.name}`.")

        elif option == "Disable":
            collection.replace_one({"guild_id": ctx.guild.id}, {"guild_id": ctx.guild.id, "option": "Disable"}, upsert=True)
            await ctx.respond(f"Anti toxicity has been disabled for `{ctx.guild.name}`.")
                
                
                





    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def add_toxic_words(self, ctx, word: Option(str, "The word that will be detected as a toxic word")):
        
        client = MongoClient("mongodb+srv://User:PASSWORD@cluster0.fdd0q.mongodb.net/DB_NAME?retryWrites=true&w=majority")
        db = client.THEDATABASE
        collection = db.antitoxicity
        collection2 = db.toxic_words
        
        #if the collection is empty or it the option is set to "disable"
        if collection.count_documents({"guild_id": ctx.guild.id}) == 0 or collection.find_one({"guild_id": ctx.guild.id})["option"] == "Disable":

                
            await ctx.respond(f"Anti toxicity is disabled or not set for `{ctx.guild.name}`. Please enable it first.")
            
        else:
    
            if collection2.find_one({"guild_id": ctx.guild.id, "word": word}):
                await ctx.respond(f"`{word}` is already in the database.")
            else:
                #add the word to the database
                collection2.insert_one({"guild_id": ctx.guild.id, "word": word})
                await ctx.respond(f"`{word}` has been added to the database.")

            
            
            
            

                
                
            
    @commands.Cog.listener()
    async def on_message(self, message: Message):
            
        client = MongoClient("mongodb+srv://User:PASSWORD@cluster0.fdd0q.mongodb.net/DB_NAME?retryWrites=true&w=majority")
        db = client.THEDATABASE
        collection = db.antitoxicity
        collection2 = db.toxic_words


        #if message author is a bot
        if message.author.bot:
            return

        else:
            
            #if the guild_id is in the database, let's see if the option is enabled
            
            try:
                    
                if collection.find_one({"guild_id": message.guild.id})["option"] == "Enable":
                    #if the message contains a word from the collection2, delete it.
                    if collection2.find_one({"guild_id": message.guild.id, "word": message.content}):
                        await message.delete()
                        await message.channel.send(f"{message.author.mention} Please refrain from using toxic words. Toxic words are prohibited in this server.")
                        return
                    
            except:
                pass          




                    
                    
def setup(bot):
	bot.add_cog(toxicity(bot))
