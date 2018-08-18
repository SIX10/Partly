import discord
from discord.ext import commands
import asyncio
import aiohttp
import random
import logging
import os

class Shitposts:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daddy(self, ctx):
        """Whos the father?"""
        await ctx.send("SIX10#0877 is my daddy")

    @commands.command()
    async def ianiq(self, ctx):
        """Ian"""
        await ctx.send("Ian's current IQ is 20.")

    @commands.command()
    async def brap(self, ctx):
        """Stinky"""
        await ctx.send("BRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP")

def setup(bot):
    bot.add_cog(Shitposts(bot))
