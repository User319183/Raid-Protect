import discord, os, sys, json, asyncio, re, string, datetime
from discord.ext import commands
from discord import activity, option
from discord.commands import Option
from discord.ext import *
from discord.ext.commands import *
from ctypes import *
from discord import Message
from pymongo import MongoClient





class Log(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def logchannel(self, ctx, channel: Option(discord.TextChannel, "The channel to log in.")):
        
        client = MongoClient("mongodb+srv://User:PASSWORD@cluster0.fdd0q.mongodb.net/DB_NAME?retryWrites=true&w=majority")
        db = client.THEDATABASE
        collection = db.logchannel
        


        #add the channel ID to the database
        collection.replace_one({"guild_id": ctx.guild.id}, {"guild_id": ctx.guild.id, "channel_id": channel.id}, upsert=True)
        await ctx.respond(f"The log channel has been set/replaced to `{channel.name}`.")
                
                




    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        client = MongoClient("mongodb+srv://User:PASSWORD@cluster0.fdd0q.mongodb.net/DB_NAME?retryWrites=true&w=majority")
        db = client.THEDATABASE
        collection = db.logchannel
        
        
        #if the collection is empty
        if collection.count_documents({"guild_id": before.guild.id}) == 0:
            return

        else:
            
        
            if after.author.bot:
                return
            
            #get the ID of the channel from the collection for the guild
            channel_id = collection.find_one({"guild_id": after.guild.id})["channel_id"]

                
            #let's create the embed
            embed = discord.Embed(title="Message Edited", description=f"{after.author.mention} edited their message in {after.channel.mention}.", color=discord.Color.blue())
            embed.add_field(name="Before", value=before.content, inline=False)
            embed.add_field(name="After", value=after.content, inline=False)
            embed.set_footer(text=f"{after.author.name}#{after.author.discriminator}")
            embed.timestamp = datetime.datetime.utcnow()
            await self.bot.get_channel(channel_id).send(embed=embed)



    #make an on_message_delete event
    @commands.Cog.listener()
    async def on_message_delete(self, message):

        
        client = MongoClient("mongodb+srv://User:PASSWORD@cluster0.fdd0q.mongodb.net/DB_NAME?retryWrites=true&w=majority")
        db = client.THEDATABASE
        collection = db.logchannel
        
        
        #if the collection is empty
        if collection.count_documents({"guild_id": message.guild.id}) == 0:
            return

        else:
            
        
            if message.author.bot:
                return
            
            #get the ID of the channel from the collection for the guild
            channel_id = collection.find_one({"guild_id": message.guild.id})["channel_id"]
                
            #let's create the embed
            embed = discord.Embed(title="Message Deleted", description=f"{message.author.mention} deleted their message in {message.channel.mention}.", color=discord.Color.red())
            embed.add_field(name="Deleted Content", value=message.content, inline=False)
            embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}")
            embed.timestamp = datetime.datetime.utcnow()
            await self.bot.get_channel(channel_id).send(embed=embed)

def setup(bot):
	bot.add_cog(Log(bot))
