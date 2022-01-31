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





class toxicity(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    
    
    
    
    
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def toxicity_mode_on(self, ctx: commands.Context):

        with open("cogs/toxicity.txt", "w+") as file:
                file.truncate(0)
                file.write("on")
                await ctx.send("Toxicity-Mode has been activated. Ready to protect.")
                
                
                
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def toxicity_mode_off(self, ctx: commands.Context):

        with open("cogs/toxicity.txt", "w+") as file:
                file.truncate(0)
                file.write("off")
                await ctx.send("toxicity-Mode has been turned off. Protection has been lost.")
                

                
                
                
                




    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if message.author.bot:
            return

        toxic_words = "you suck", "u suck"

        with open("cogs/toxicity.txt", "r+") as file:
            for lines in file:
                if "on" in lines:
                    if message.content in toxic_words:
                        await message.delete()
                        await message.channel.send(f"{message.author.mention} has said toxic phrases/words !")
                        await message.author.send("Toxic words are prohibited!")
                        
                else:
                    break
                        
                        
                        
 
 




                    
                    
def setup(bot):
	bot.add_cog(toxicity(bot))