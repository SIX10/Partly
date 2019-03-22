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
    async def jenkins(self, ctx):
        await ctx.send("Jenkins is one big ole poo poo head.")

    @commands.command()
    async def daddy(self, ctx):
        await ctx.send("SIX10#0877 is my daddy")

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("*sticks finger up ass*")

    @commands.command()
    async def ianiq(self, ctx):
        with open("ianiq.txt", "r") as fp:
            iq = fp.read()
        newiq = int(iq)
        newiq -= 1
        with open("ianiq.txt", "w") as fpp:
            fpp.write(str(newiq))
        await ctx.send(str(newiq))

    @commands.command()
    async def brap(self, ctx):
        await ctx.send("BRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP")

    @commands.command()
    async def london(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=gYs37prLHGc")



def setup(bot):
    bot.add_cog(Shitposts(bot))
