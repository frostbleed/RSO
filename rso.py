import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client  = discord.Client()
client = commands.Bot(command_prefix = "!")
@client.event
async def on_ready():
    print("Radio Switchboard Operator Active")
    await client.change_presence(game=discord.Game(name="STATUS: CENTCOM Online"))

@client.event
async def on_message(message):
    if message.content.startswith("!daycare"):
        msg = "\"This is SWAT, not daycare.\" - NCISrox"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!cmds"):
        msg = "**!cmds**: Display the list of commands."
        await client.send_message(message.channel, msg)
    if message.content.startswith("tell bloo to shut"):
        msg = "bloo shut"
        await client.send_message(message.channel, msg)
client.run(os.getenv('TOKEN'))
