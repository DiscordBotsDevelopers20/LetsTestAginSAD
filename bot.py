# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

client = Bot(description="Basic Bot by Habchy#1665", command_prefix="-" pm_help = False)

@client.event
async def on_ready():
	
	print('--------')
	print('Created by Scanner#4797')
    await client.change_presence(game=discord.Game(name="-HELP | YOU", type=3))

@client.command()
async def ping(*args):

	await client.say(":ping_pong: Pong!")
	await asyncio.sleep(3)
	await client.say(":warning: This bot was created by **Habchy#1665**, it seems that you have not modified it yet. Go edit the file and try it out!")
	
client.run(process.env.BOT_TOKEN)

