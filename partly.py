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
    await bot.change_presence(game=discord.Game(name="My pronoun is +"))

@bot.command()
async def add(a: int, b: int):
    await bot.say(a+b)

@bot.command()
async def multiply(a: int, b: int):
    await bot.say(a*b)

@bot.command()
async def divide(a: int, b: int):
    await bot.say(a/b)

@bot.command()
async def subtract(a: int, b: int):
    await bot.say(a-b)

@bot.command()
async def troll():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://rolloffle.churchburning.org/troll_me_text.php") as site:
            if site.status == 200:
                await bot.say(await site.text())
            else:
                await bot.say("Could not connect.")



@bot.command()
async def invite():
    msg = discord.Embed(title="Invite",
                        description="You can invite me to your server with https://discordapp.com/oauth2/authorize?client_id=447940688508878868&scope=bot&permissions=0",
                        color=discord.Color.red())
    await bot.say(embed=msg)


@bot.command()
async def help():
    msg = discord.Embed(title="Help",
                        description="Partly's commands are found at https://github.com/SIX10/Partly/blob/master/Help.md",
                        color=discord.Color.red())
    await bot.say(embed=msg)

bot.run(token)
