import discord
from discord.ext import commands
import asyncio
import aiohttp
import random

negros = ["Whats wrong with black people?" , "Stop eating all of the watermelon, you ape" , "Wakanda forever" , "Ooga Booga" , "I bless the rains down in Africa!" , "Niggers are just white people painted by God so he knows who the bad ones are" , "Black people don't exist" , "I ran over a CIA Nigger with my car" , "I just wanna ride on the front of the bus" , "Black people? You mean monkeys?"]

token= ""

bot = commands.Bot(command_prefix="+", description="A bot that does stuff. By SIX10#0877.")
@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("-----------")
    await bot.change_presence(game=discord.Game(name="yo girl | +commands "))



# Math
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

#Fun
@bot.command()
async def troll():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://rolloffle.churchburning.org/troll_me_text.php") as site:
            if site.status == 200:
                await bot.say(await site.text())
            else:
                await bot.say("Could not connect.")

@bot.command()
async def godsays():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://templeos.net/") as site:
            if site.status == 200:
                await bot.say(await site.text())
            else:
                await bot.say("Could not connect to heaven.")

@bot.command()
async def brap():
    await bot.say("BRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP")

@bot.command()
async def negra():
    negrachoice = random.choice(negros)
    await bot.say(negrachoice)
#Misc
@bot.command()
async def invite():
    msg = discord.Embed(title="Invite",
                        description="You can invite me to your server with https://discordapp.com/oauth2/authorize?client_id=447940688508878868&scope=bot&permissions=0",
                        color=discord.Color.red())
    await bot.say(embed=msg)


@bot.command()
async def commands():
    msg = discord.Embed(title="Commands",
                        description="Partly's commands are found at https://github.com/SIX10/Partly/blob/master/Help.md",
                        color=discord.Color.red())
    await bot.say(embed=msg)

bot.run(token)
