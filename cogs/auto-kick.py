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





class Autokick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    
    
    
    
    
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def autokick_mode_on(self, ctx: commands.Context):

        with open("cogs/autokick.txt", "w+") as file:
                file.truncate(0)
                file.write("on")
                await ctx.send("Autokick-Mode has been activated. Ready to protect.")
                
                
                
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def autokick_mode_off(self, ctx: commands.Context):

        with open("cogs/autokick.txt", "w+") as file:
                file.truncate(0)
                file.write("off")
                await ctx.send("Autokick-Mode has been turned off. Protection has been lost.")
                

                
                
                
                




    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.bot:
            return


        with open("cogs/autokick.txt", "r+") as file:
            for lines in file:
                if "on" in lines:
                    await member.send("This server is protected by the module **auto-kick**. New users are not allowed to join this server.")
                    await member.kick()
  
  
  
def setup(bot):
	bot.add_cog(Autokick(bot))
