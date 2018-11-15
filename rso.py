import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import datetime

Client  = discord.Client()
client = commands.Bot(command_prefix = "!")
@client.event
async def on_ready():
    print("Radio Switchboard Operator Active")
    await client.change_presence(game=discord.Game(name="STATUS: CENTCOM Online"))

form = "deploywarn"
waitingForConfirmation = False
threat = "drill"
region = "las vegas"
host = "3616260"

@client.event
async def on_message(message):
    global waitingForConfirmation
    global threat
    global region
    global host
    global form
    timestamp = str(datetime.datetime.now())
    timestamp = timestamp.split(" ")
    try:
        deploymsg = ('''<:swat:511794129999626270> <:usa:511794381406208000> __**DEPLOYMENT ORDER**__ <:usa:511794381406208000> <:swat:511794129999626270>
**DATE: **``''' + timestamp[0] + '''``
**TIME: **``''' + timestamp[1] + " GMT" + '''``
**TYPE: **``''' + threat.upper() + '''``
**LOCATION: **``''' + region.upper() + '''``
        
ALL UNITS ARE ORDERED TO **DEPLOY** TO THE CITY OF ''' + region.upper() + "." + '''
ALL UNITS SHALL RESPOND **WITHIN FIVE (5) MINUTES** AND REMAIN SILENT UPON ARRIVAL.
        
FOLLOW THE ADMINISTRATOR IN CHARGE IMMEDIATELY:''' + "\nhttps://www.roblox.com/users/" + host + "/profile"  + "\n<@&everyone>")
    except:
        print("deployment message error")
    if message.content.startswith("!daycare"):
        msg = "\"This is SWAT, not daycare.\" - NCISrox"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!cmds"):
        msg = """**!cmds**: Display a list of commands.
**!deploy**: Issue a deployment order. Format: !deploy <drill/emergency> <lv/dc> <user id>"""
        await client.send_message(message.channel, msg)
    if message.content.startswith("!confirm"):
        if waitingForConfirmation:
            try:
                splitreq = (message.content).split(" ")
                if((splitreq[1] == "drilldeploy") and (threat == "drill") and (form == "deploy")):
                    msg = "(insert drill deployment text here)"
                    await client.send_message(discord.Object(id='511736808544010275'), deploymsg)
                    await client.send_message(message.channel, "Deployment announced. Lead with pride and dignity. Good luck.")
                elif((splitreq[1] == "emergdeploy") and (threat == "emergency") and (form == "deploy")):
                    msg = "(insert emergency deployment text here)"
                    await client.send_message(discord.Object(id='511736808544010275'), deploymsg)
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
                    region = "las vegas"
                    host = splitreq[3]
                    waitingForConfirmation = True
                    msg = "**READ CAREFULLY AND CONFIRM WITH !confirm drilldeploy**:\n``DRILL DEPLOYMENT REQUEST TO LAS VEGAS, HOSTED BY " + splitreq[3] + "``" + "\n\n**ENSURE YOU ARE AT LAS VEGAS PRIOR TO CONFIRMING**\n**IF INCORRECT, RETYPE DEPLOY COMMAND**"
                elif(splitreq[2] == "dc"):
                    form = "deploy"
                    threat = "drill"
                    region = "washington dc"
                    host = splitreq[3]
                    waitingForConfirmation = True
                    msg = "**READ CAREFULLY AND CONFIRM WITH !confirm drilldeploy**:\n``DRILL DEPLOYMENT REQUEST TO WASHINGTON DC, HOSTED BY " + splitreq[3] + "``" + "\n\n**ENSURE YOU ARE AT WASHINGTON DC PRIOR TO CONFIRMING**\n**IF INCORRECT, RETYPE DEPLOY COMMAND**"
                else:
                    msg = "Invalid deployment request. Format: !deploy <drill/emergency> <lv/dc> <id>"
            elif (splitreq[1] == "emergency"):
                if(splitreq[2] == "lv"):
                    form = "deploy"
                    threat = "emergency"
                    region = "las vegas"
                    host = splitreq[3]
                    waitingForConfirmation = True
                    msg = "**READ CAREFULLY AND CONFIRM WITH !confirm emergdeploy**:\n``EMERGENCY DEPLOYMENT REQUEST TO LAS VEGAS, HOSTED BY " + splitreq[3] + "``" + "\n\n**ENSURE YOU ARE AT LAS VEGAS PRIOR TO CONFIRMING**\n**IF INCORRECT, RETYPE DEPLOY COMMAND**"
                elif(splitreq[2] == "dc"):
                    form = "deploy"
                    threat = "emergency"
                    region = "washington dc"
                    host = splitreq[3]
                    waitingForConfirmation = True
                    msg = "**READ CAREFULLY AND CONFIRM WITH !confirm emergdeploy**:\n``EMERGENCY DEPLOYMENT REQUEST TO WASHINGTON DC, HOSTED BY " + splitreq[3] + "``" + "\n\n**ENSURE YOU ARE AT WASHINGTON DC PRIOR TO CONFIRMING**\n**IF INCORRECT, RETYPE DEPLOY COMMAND**"
                else:
                    msg = "Invalid deployment request. Format: !deploy <drill/emergency> <lv/dc> <user id>"
            else:
                msg = "Invalid deployment request. Format: !deploy <drill/emergency> <lv/dc> <user id>"
        except IndexError:
            msg = "Invalid deployment request. Format: !deploy <drill/emergency> <lv/dc> <user id>"
        await client.send_message(message.channel, msg)
client.run(os.getenv('TOKEN'))
