import discord
from discord.ext import commands
import asyncio
import aiohttp
import random
import logging
import os

class Media:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def webm(self, ctx):
        """Pulls a Webm from my collection, submit more at Partly's Discord (p+bug)"""
        randomwebm = random.choice(os.listdir("Webms//"))
        await ctx.send(file=discord.File("Webms//" + randomwebm))

    @commands.command()
    async def cursed(self, ctx):
        """Pulls a cursed image from my collection, submit more at Partly's Discord (p+bug)"""
        randomcursed = random.choice(os.listdir("cursedImages//"))
        await ctx.send(file=discord.File("cursedImages//" + randomcursed))

def setup(bot):
    bot.add_cog(Media(bot))
