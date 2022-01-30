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





class Invites(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    
    
    
    
    
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def invites_mode_on(self, ctx: commands.Context):

        with open("cogs/invites.txt", "w+") as file:
                file.truncate(0)
                file.write("on")
                await ctx.send("Invites-Mode has been activated. Ready to protect.")
                
                
                
                
                
                
        
        
               
               
               
                
                
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def invites_mode_off(self, ctx: commands.Context):

        with open("cogs/invites.txt", "w+") as file:
                file.truncate(0)
                file.write("off")
                await ctx.send("Invites-Mode has been turned off. Protection has been lost.")
                

                
                
                
                




    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if message.author.bot:
            return


        with open("cogs/invites.txt", "r+") as file:
            for lines in file:
                if "on" in lines:
                    if "discord.gg/" in message.content:
                        await message.channel.send(f"{message.author.mention} has sent an invite !")
                        await message.author.send("Discord invites are prohibited!")
                        await message.delete()
                        
                else:
                    break
  
  
  
def setup(bot):
	bot.add_cog(Invites(bot))
