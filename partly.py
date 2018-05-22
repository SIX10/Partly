import discord
from discord.ext import commands
import asyncio
import aiohttp
import random


token= ""

bot = commands.Bot(command_prefix="+", description="A bot that does stuff. By SIX10#0877.")
@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("-----------")
    await bot.change_presence(activity=discord.Game(name="with yo girl | +commands "))



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
async def quit(ctx):
    if ctx.author.id == 130853292275269632:
        await ctx.send("Shutting down...")
        await bot.logout()
    else: await ctx.send("You aren't my owner!")

bot.run(token)
