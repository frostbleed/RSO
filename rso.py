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

form = "deploywarn"
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
    global form
    if message.content.startswith("!daycare"):
        msg = "\"This is SWAT, not daycare.\" - NCISrox"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!cmds"):
        msg = """**!cmds**: Display the list of commands.
**!deploy**: Issue a deployment order. Format: !deploy <drill/emergency> <lv/dc> <name>"""
        await client.send_message(message.channel, msg)
    if message.content.startswith("!confirm"):
        if waitingForConfirmation:
            try:
                splitreq = (message.content).split(" ")
                if((splitreq[1] == "drilldeploy") and (threat == "drill") and (form == "deploy")):
                    msg = "(insert drill deployment text here)"
                    await client.send_message(discord.Object(id='511736808544010275'), msg)
                    await client.send_message(message.channel, "Deployment announced. Lead with pride and dignity. Good luck.")
                elif((splitreq[1] == "emergdeploy") and (threat == "emergency") and (form == "deploy")):
                    msg = "(insert emergency deployment text here)"
                    await client.send_message(discord.Object(id='511736808544010275'), msg)
                    await client.send_message(message.channel, "Deployment announced. Lead with pride and dignity. Good luck.")
                else:
                    msg = "Invalid confirmation."
                    await client.send_message(message.channel, msg)
            except IndexError:
                msg = "Invalid confirmation."
                await client.send_message(message.channel, msg)
    if message.content.startswith("!deploy"):
        req = message.content
        splitreq = req.split(" ")
        try:
            if (splitreq[1] == "drill"):
                if(splitreq[2] == "lv"):
                    form = "deploy"
                    threat = "drill"
                    region = "lv"
                    host = splitreq[3]
                    waitingForConfirmation = True
                    msg = "**READ CAREFULLY AND CONFIRM WITH !confirm drilldeploy**:\n``DRILL DEPLOYMENT REQUEST TO LAS VEGAS, HOSTED BY " + splitreq[3] + "``" + "\n\n**ENSURE YOU ARE AT LAS VEGAS PRIOR TO CONFIRMING**\n**IF INCORRECT, RETYPE DEPLOY COMMAND**"
                elif(splitreq[2] == "dc"):
                    form = "deploy"
                    threat = "drill"
                    region = "dc"
                    host = splitreq[3]
                    waitingForConfirmation = True
                    msg = "**READ CAREFULLY AND CONFIRM WITH !confirm drilldeploy**:\n``DRILL DEPLOYMENT REQUEST TO WASHINGTON DC, HOSTED BY " + splitreq[3] + "``" + "\n\n**ENSURE YOU ARE AT WASHINGTON DC PRIOR TO CONFIRMING**\n**IF INCORRECT, RETYPE DEPLOY COMMAND**"
                else:
                    msg = "Invalid deployment request. Format: !deploy <drill/emergency> <lv/dc> <name>"
            elif (splitreq[1] == "emergency"):
                if(splitreq[2] == "lv"):
                    form = "deploy"
                    threat = "emergency"
                    region = "lv"
                    host = splitreq[3]
                    waitingForConfirmation = True
                    msg = "**READ CAREFULLY AND CONFIRM WITH !confirm emergdeploy**:\n``EMERGENCY DEPLOYMENT REQUEST TO LAS VEGAS, HOSTED BY " + splitreq[3] + "``" + "\n\n**ENSURE YOU ARE AT LAS VEGAS PRIOR TO CONFIRMING**\n**IF INCORRECT, RETYPE DEPLOY COMMAND**"
                elif(splitreq[2] == "dc"):
                    form = "deploy"
                    threat = "emergency"
                    region = "dc"
                    host = splitreq[3]
                    waitingForConfirmation = True
                    msg = "**READ CAREFULLY AND CONFIRM WITH !confirm emergdeploy**:\n```EMERGENCY DEPLOYMENT REQUEST TO WASHINGTON DC, HOSTED BY " + splitreq[3] + "``" + "\n\n**ENSURE YOU ARE AT WASHINGTON DC PRIOR TO CONFIRMING**\n**IF INCORRECT, RETYPE DEPLOY COMMAND**"
                else:
                    msg = "Invalid deployment request. Format: !deploy <drill/emergency> <lv/dc> <name>"
            else:
                msg = "Invalid deployment request. Format: !deploy <drill/emergency> <lv/dc> <name>"
        except IndexError:
            msg = "Invalid deployment request. Format: !deploy <drill/emergency> <lv/dc> <name>"
        await client.send_message(message.channel, msg)
client.run(os.getenv('TOKEN'))
