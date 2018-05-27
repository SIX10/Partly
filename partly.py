import discord
from discord.ext import commands
import asyncio
import aiohttp
import random
import logging
import os

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


<<<<<<< HEAD



=======
>>>>>>> b87f0e198bf9a214c21b654d836eacd986b5105f
token= ""

if not discord.opus.is_loaded():
    discord.opus.load_opus()


bot = commands.Bot(command_prefix="+", description="A bot that does stuff. By SIX10#0877.")
@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("-----------")
    await bot.change_presence(activity=discord.Game(name="with yo girl | +commands "))

    bot.load_extension("music")


# Math
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def divide(ctx, a: int, b: int):
    if b == 0:
        await ctx.send("Cannot divide by zero.")
    else:
        await ctx.send(a/b)

@bot.command()
async def subtract(ctx, a: int, b: int):
    await ctx.send(a-b)

#Fun
@bot.command()
async def troll(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("http://rolloffle.churchburning.org/troll_me_text.php") as site:
            if site.status == 200:
                await ctx.send(await site.text())
            else:
                await ctx.send("Could not connect.")

@bot.command()
async def godsays(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://templeos.net/") as site:
            if site.status == 200:
                await ctx.send(await site.text())
            else:
                await ctx.send("Could not connect to heaven.")

@bot.command()
async def brap(ctx):
    await ctx.send("BRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP")

<<<<<<< HEAD


=======
>>>>>>> b87f0e198bf9a214c21b654d836eacd986b5105f
@bot.command()
async def ianiq(ctx):
    await ctx.send("Ian Bertand's current IQ is 20.")

@bot.command()
async def hello(ctx):
    await ctx.send("*sticks finger up ass*")
#Misc
@bot.command()
async def invite(ctx):
    msg = discord.Embed(title="Invite",
                        description="You can invite me to your server with https://discordapp.com/oauth2/authorize?client_id=447940688508878868&scope=bot&permissions=0",
                        color=discord.Color.red())
    await ctx.send(embed=msg)


@bot.command()
async def commands(ctx):
    msg = discord.Embed(title="Commands",
                        description="Partly's commands are found at https://github.com/SIX10/Partly/blob/master/Help.md",
                        color=discord.Color.red())
    await ctx.send(embed=msg)

@bot.command()
async def servers(ctx):
    msg = "Connected to " + str(len(bot.guilds)) + " servers"
    await ctx.send(msg)


@bot.command()
async def quit(ctx):
    if ctx.author.id == 130853292275269632:
        await ctx.send("Shutting down...")
        await bot.logout()



bot.run(token)
