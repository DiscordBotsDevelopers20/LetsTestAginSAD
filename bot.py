import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import random
import time
import datetime
import os

client = discord.Client()
bot_prefix= ">"
client = commands.Bot(command_prefix=bot_prefix)




@client.event
async def on_ready():
    print("TO Bot Official")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await asyncio.sleep (1)
    await client.change_presence(game=discord.Game(name='>HELP ', type=0))
   

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith(">id"):
        await client.send_message(message.channel, "**Name:-** {} \n \n **ID:-** {} " .format (message.author , message.author.id))


client.run(os.getenv("TOKEN"))

