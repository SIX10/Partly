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

token= "NDQ3OTQwNjg4NTA4ODc4ODY4.DfapCw.eE4B4iEftfQisVZzpTtajZWIbMs"

if not discord.opus.is_loaded():
    discord.opus.load_opus()

cogs = ['cogs.music',
        'cogs.fun',
        'cogs.media',
        'cogs.shitposts',
        'cogs.4chanMarkov.py']

bot = commands.Bot(command_prefix="p+", description="A bot that does stuff. By SIX10#0877.")
@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("-----------")
    await bot.change_presence(activity=discord.Game(name="with yo girl | p+commands "))

    for cog in cogs:
        bot.load_extension(cog)

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
async def users(ctx):
    msg = "Serving " + str(len(bot.users)) + " users"
    await ctx.send(msg)

@bot.command()
async def bug(ctx):
    await ctx.send("Found a bug? Report it to https://discord.gg/7KWqhzb or message SIX10#0877")

@bot.command(hidden=True)
async def listservers(ctx):
    if ctx.author.id == 130853292275269632:
        msg = "Connected to " + str(bot.guilds)
        await ctx.send (msg)

@bot.command(hidden=True)
async def quit(ctx):
    if ctx.author.id == 130853292275269632:
        await ctx.send("Shutting down...")
        await bot.logout()

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! Responded in {round(bot.latency*1000, 2)} ms")

@bot.command(name='reload', hidden=True)
async def cog_reload(self, ctx, *, cog: str):
    if ctx.author.id == 130853292275269632:
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')
bot.run(token)
