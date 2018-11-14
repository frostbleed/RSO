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

waitingForConfirmation = False
threat = "drill"
region = "lv"
host = "frostbleed"

@client.event
async def on_message(message):
    global waitingForConfirmation
    global threat
    global region
    global host
    if message.content.startswith("!daycare"):
        msg = "\"This is SWAT, not daycare.\" - NCISrox"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!cmds"):
        msg = """**!cmds**: Display the list of commands.
**!deploy**: Issue a deployment order."""
        await client.send_message(message.channel, msg)
    if message.content.startswith("!deploy"):
        req = string((message.content).lower)
        splitreq = req.split(" ")
        if (splitreq[1] == "drill"):
            if(splitreq[2] == "lv"):
                threat = "drill"
                region = "lv"
                host = splitreq[3]
                msg = "**READ CAREFULLY AND CONFIRM WITH !confirm**: ``DRILL DEPLOYMENT REQUEST TO LV, HOSTED BY" + splitreq[3] + "``"
            elif(splitreq[2] == "dc"):
                threat = "drill"
                region = "dc"
                host = splitreq[3]
                msg = "**READ CAREFULLY AND CONFIRM WITH !confirm**: ``DRILL DEPLOYMENT REQUEST TO DC, HOSTED BY" + splitreq[3] + "``"
            else:
                msg = "Invalid deployment request. Format: !deploy <drill/emergency> <lv/dc> <name>"
        elif (splitreq[1] == "emergency"):
            if(splitreq[2] == "lv"):
                threat = "emergency"
                region = "lv"
                host = splitreq[3]
                msg = "**READ CAREFULLY AND CONFIRM WITH !confirm**: ``EMERGENCY DEPLOYMENT REQUEST TO LV, HOSTED BY" + splitreq[3] + "``"
            elif(splitreq[2] == "dc"):
                threat = "emergency"
                region = "dc"
                host = splitreq[3]
                msg = "**READ CAREFULLY AND CONFIRM WITH !confirm**: ``EMERGENCY DEPLOYMENT REQUEST TO DC, HOSTED BY" + splitreq[3] + "``"
            else:
                msg = "Invalid deployment request. Format: !deploy <drill/emergency> <lv/dc> <name>"
        await client.send_message(message.channel, msg)
client.run(os.getenv('TOKEN'))
