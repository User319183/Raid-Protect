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





class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    
    
    
    
    
    @commands.command()
    async def help(self, ctx: commands.Context):               
        command_prefix= "ar-" #your bots prefix here and in "main.py"
                        
        embed = discord.Embed(title="Bot Info", description="My help panel", color=0xD708CC)
        embed.add_field(name="__Bot Creators:__", value="User319183#3149 \n Thewizz1338#6367", inline=True) # please don't remove credits!!
        embed.add_field(name="__Modules:__", value=f"anti-spam \n anti-invites \n anti-toxicity \n auto-kick \n bad-word-blocking \n log-mode")
        embed.add_field(name="__Module commands:__", value = f"{command_prefix}spam_mode_on \n {command_prefix}spam_mode_off \n {command_prefix}invites_mode_on \n {command_prefix}invites_mode_off \n {command_prefix}toxicity_mode_on \n {command_prefix}toxicity_mode_off \n {command_prefix}autokick_mode_on \n {command_prefix}autokick_mode_off \n {command_prefix}badwordblocker \n {command_prefix}log_mode_on \n {command_prefix}log_mode_off", inline = False)


        await ctx.send(embed=embed)
 



                    
                    
def setup(bot):
	bot.add_cog(Help(bot))