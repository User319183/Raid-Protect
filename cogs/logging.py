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






class Log(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    
    
    
    
    
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def log_mode_on(self, ctx: commands.Context):

        with open("cogs/log.txt", "w+") as file:
                file.truncate(0)
                file.write("on")
                await ctx.send("Log-Mode has been activated. Ready to protect.")
                
                
                
                
                
                
        
        
               
               
               
                
                
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def log_mode_off(self, ctx: commands.Context):

        with open("cogs/log.txt", "w+") as file:
                file.truncate(0)
                file.write("off")
                await ctx.send("Log-Mode has been turned off. Protection has been lost.")
                

                
                
                
                




    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if after.author.bot:
            return


        with open("cogs/log.txt", "r+") as file:
            for lines in file:
                if "on" in lines:
                    if before.content == after.content:
                        return
                    try:

                        log_channel = discord.utils.get(before.guild.text_channels, name="logs")
  
                        if before.author.bot == True:
                            return
                        embed = discord.Embed(title="Message Edit", description=f"{before.author.mention} edited a message", color=3447003)
                        embed.add_field(name="Before Edit:", value=before.content, inline=False)
                        embed.add_field(name="After Edit:", value=after.content, inline=False)
                        embed.add_field(name="Channel:", value=after.channel.mention, inline=False)
                        await log_channel.send(embed=embed)

                    except:
                        pass
  
  

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        with open("cogs/log.txt", "r+") as file:
            for lines in file:
                if "on" in lines:
                    try:

                        log_channel = discord.utils.get(message.guild.text_channels, name="logs")
   
                        if message.author.bot == True:
                            return
                        embed = discord.Embed(title="Message Delete", description=f"{message.author.mention} deleted a message", color=15158332)
                        embed.add_field(name="Deleted Message:", value=message.content, inline=False)
                        embed.add_field(name="Channel:", value=message.channel.mention, inline=False)
                        await log_channel.send(embed=embed)

                    except:
                        pass

    
    
    
    
    
    
    
def setup(bot):
	bot.add_cog(Log(bot))