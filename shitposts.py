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
    async def jenkins(ctx):
        await ctx.send("Jenkins is one big ole poo poo head.")

    @commands.command()
    async def fucken(ctx):
        await ctx.send("Ay you im gonna fuckin NAYNAY on this bitch fuck nigga as jew OK dont fucking mess with me or you will fucking regret it bucko you fuckin sauck my pp right nowe or face the concequences kid ok you follow my rules or you follow the road ok no fucking stick a straw up my ass aand suck and suck as hard and long as you can or im going to MMMMHMMMMMMMmmm praAISe the lord you ok now fucking get your Stoopid ass bitch ass face right here right now before i OOOAHHHHyaaa it mhmmm that was the LAST STRAW before I NUT On your face LIKE i did to jess down the street mmhmmm baby!")

    @commands.command()
    async def daddy(ctx):
        await ctx.send("SIX10#0877 is my daddy")

    @commands.command()
    async def hello(ctx):
        await ctx.send("*sticks finger up ass*")

    @commands.command()
    async def ianiq(ctx):
        await ctx.send("Ian Bertand's current IQ is 20.")


def setup(bot):
    bot.add_cog(Shitposts(bot))