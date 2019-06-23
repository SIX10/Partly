import discord
from discord.ext import commands
import asyncio
import aiohttp
import random
import logging
import os

class Fun:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def troll(self, ctx):
        """funny saying hehehe"""
        async with aiohttp.ClientSession() as session:
            async with session.get("http://rolloffle.churchburning.org/troll_me_text.php") as site:
                if site.status == 200:
                    await ctx.send(await site.text())
                else:
                    await ctx.send("Could not connect.")


def setup(bot):
    bot.add_cog(Fun(bot))
