import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import random
import time
import datetime
import os

bot = discord.Client()
bot_prefix= ">"
bot = commands.Bot(command_prefix=bot_prefix)




@bot.event
async def on_ready():
    print("TO Bot Official")
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    await asyncio.sleep (1)
    await bot.change_presence(game=discord.Game(name="Scanner's Server", type=3))
   
@bot.event
async def on_member_join(member):
    server = member.server

    if server.id == "418001869781205002":
        channel = bot.get_channel("418001869781205004")
        msg = "**:tada: Welcome {} To {} , You are the {} User!**".format(member.mention ,member.server.name, len(server.members))
        await bot.send_message(channel, msg)
        
    else:
        return


bot.run(os.getenv("TOKEN"))

