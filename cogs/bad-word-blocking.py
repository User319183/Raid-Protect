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


class badwordblocker(commands.Cog):


    def __init__(self, bot: commands.Bot):
        self.bot = bot










    @commands.command()
    async def badwordblocker(self, ctx: commands.Context):

        await ctx.send("""Need a Discord bad word blocking bot? Unfortunately, this bot does not come with a pre-built filter. Instead, you can try out our open source simple bad word blocking bot on github: <https://github.com/User319183/Simple_badwordblocker.py> 
                       \n Or would you like to try out our advanced Discord bad word blocking bot? Go to <https://profanityblocker.org> and read everything there!""")
                
                






def setup(bot: commands.Bot):
    bot.add_cog(badwordblocker(bot))