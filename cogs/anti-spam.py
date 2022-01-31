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


class AntiSpam(commands.Cog):
    """A simple, basic cog."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot










    @commands.command()
    @commands.has_permissions(administrator=True)
    async def spam_mode_on(self, ctx: commands.Context):

        with open("cogs/spammode.txt", "w+") as file:
                file.truncate(0)
                file.write("on")
                await ctx.send("Spam-Mode has been activated. Ready to protect.")
                
                
                
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def spam_mode_off(self, ctx: commands.Context):

        with open("cogs/spammode.txt", "w+") as file:
                file.truncate(0)
                file.write("off")
                await ctx.send("Spam-Mode has been turned off. Protection has been lost.")




    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if message.author.bot:
            return

        with open("cogs/spammode.txt", "r+") as file:
        
            for lines in file:
                if "on" in lines:

                    counter = 0
                    with open("cogs/spamdetect.txt", "r+") as file:
                        for lines in file:
                            if lines.strip("\n") == str(message.author.id):
                                counter+=1

                        file.writelines(f"{str(message.author.id)}\n")

                        if counter > 5:
                            await message.author.send("Spam is prohibited. You have been kicked.")
                            await message.author.kick()
                            print("action = kicked")
                            await message.channel.purge(limit=5)
                
                
                            
                            try:

                                channel = discord.utils.get(message.guild.text_channels, name="spam-logs")
                                message.author

                                embed = discord.Embed(title="Member Kicked", description=f"{message.author.mention} has been punished for spam.", color=0xD708CC)
                                embed.add_field(name="Action", value=f"Kicked", inline=False)
                                embed.timestamp = discord.utils.utcnow()
                                await channel.send(embed=embed)
                            except:
                                pass
                            
                            
                else:
                    break






def setup(bot: commands.Bot):
    bot.add_cog(AntiSpam(bot))