import discord, os, sys, json, asyncio
from discord.ext import commands
from discord import activity
from discord.commands import Option
from pymongo import MongoClient
from discord import option
class Bypass(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def bypass_channel(self, ctx, channel: Option(discord.TextChannel, "Select a channel")):
        client = MongoClient("mongodb+srv://User:PASSWORD@cluster0.fdd0q.mongodb.net/DB_NAME?retryWrites=true&w=majority")
        db = client.THEDATABASE
        collection = db.bypass_channels
        
        #if the channel ID is already in the collection with the guild ID
        if collection.find_one({"guild_id": ctx.guild.id, "channel_id": channel.id}):
            await ctx.respond(f"{channel.mention} is already in the bypass list.")
            
        else:
            collection.insert_one({"guild_id": ctx.guild.id, "channel_id": channel.id})
            await ctx.respond(f"{channel.mention} has been added to the bypass list.")


    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def unbypass_bypass_channel(self, ctx, channel: Option(discord.TextChannel, "Select a channel")):
        client = MongoClient("mongodb+srv://User:PASSWORD@cluster0.fdd0q.mongodb.net/DB_NAME?retryWrites=true&w=majority")
        db = client.THEDATABASE
        collection = db.bypass_channels
        
        #if the channel ID is not in the collection with the guild ID
        if not collection.find_one({"guild_id": ctx.guild.id, "channel_id": channel.id}):
            await ctx.respond(f"{channel.mention} is not in the bypass list.")

        else:
            collection.delete_one({"guild_id": ctx.guild.id, "channel_id": channel.id})
            await ctx.respond(f"{channel.mention} has been removed from the bypass list.")

                
                

    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def bypass_user(self, ctx, member: Option(discord.Member, "Select a member")):
        client = MongoClient("mongodb+srv://User:PASSWORD@cluster0.fdd0q.mongodb.net/DB_NAME?retryWrites=true&w=majority")
        db = client.THEDATABASE
        collection = db.bypass_users
        
        #if the user ID is already in the collection with the guild ID
        if collection.find_one({"guild_id": ctx.guild.id, "user_id": member.id}):
            await ctx.respond(f"{member.mention} is already in the bypass list.")

                
        else:
            collection.insert_one({"guild_id": ctx.guild.id, "user_id": member.id})
            await ctx.respond(f"{member.mention} has been added to the bypass list.")

                
                
                
                
    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def unbypass_user(self, ctx, member: Option(discord.Member, "Select a member")):
        client = MongoClient("mongodb+srv://User:PASSWORD@cluster0.fdd0q.mongodb.net/DB_NAME?retryWrites=true&w=majority")
        db = client.THEDATABASE
        collection = db.bypass_users
        
        #if the user ID is not in the collection with the guild ID
        if not collection.find_one({"guild_id": ctx.guild.id, "user_id": member.id}):
            await ctx.respond(f"{member.mention} is not in the bypass list.")

                
        else:
            collection.delete_one({"guild_id": ctx.guild.id, "user_id": member.id})
            await ctx.respond(f"{member.mention} has been removed from the bypass list.")

#let's work on the view_bypass command next repository update
def setup(bot):
	bot.add_cog(Bypass(bot))
