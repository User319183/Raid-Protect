import discord

from discord.ext import commands

from discord import activity

from discord.commands import Option

import os
import sys

import json

import asyncio as asyncio


from datetime import datetime

import psutil


class Meta(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    
    
    #PLEASE DO NOT REMOVE CREDITS!! THANK YOU!!
    
    
#### Source code protected by the GNU GENERAL PUBLIC LICENSE Version 3.


# </help:COMMAND_ID> TO MENTION A COMMAND IN THE BOT!!

    
    @commands.slash_command()
    async def help(self, ctx: commands.Context):                           
        embed = discord.Embed(title="Enhanced Raid Protect help panel", description="Welcome to the new, more powerful version of Raid Protect", color=0xD708CC)
        embed.add_field(name="__Modules:__", value=f"anti spam (WIP) \n anti invites \n anti toxicity \n auto kick \n log channel")
        embed.add_field(name="For more information about the bot, do:", value=f"</info:1012467045343965276> ") #the ID i put here goes for the /info command

        await ctx.respond(embed=embed)
 


    @commands.slash_command()
    async def info(self, ctx: commands.Context):

            embed = discord.Embed(title="Bot Info", description="General information about Raid Protect", color=0xD708CC)
            embed.add_field(name="__Bot Creators:__", value="User319183#3149 \n Thewizz1338#6367 \n AnonymousDev#3773", inline=True) # please don't remove credits!!
            embed.add_field(name="__Server Count:__", value=len(self.bot.guilds), inline=True)
            all_members_embed_list = []
            for x in self.bot.get_all_members():
                all_members_embed_list.append(x)
            embed.add_field(name="__Users being watched:__", value=f"{len(all_members_embed_list)}")
            embed.add_field(name="__Websocket Ping:__", value=f"{round(self.bot.latency * 1000)}")
            embed.add_field(name="__CPU Usage:__", value = f'{psutil.cpu_percent()}%', inline = False)
            embed.add_field(name="__Memory Usage:__", value = f'{psutil.virtual_memory().percent}%', inline = False)
            embed.timestamp = datetime.utcnow()
            await ctx.respond(embed=embed)



    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, *, module: str):
        """Reloads a module."""
        try:
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send(f'```py\n{e}\n```')
        else:
            await ctx.send('\N{OK HAND SIGN}')
            

                    
                    
def setup(bot):
	bot.add_cog(Meta(bot))
