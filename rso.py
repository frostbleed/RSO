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
deploymentIsHappening = False
standbyIsHappening = False

@client.event
async def on_message(message):
    global waitingForConfirmation
    global threat
    global region
    global host
    global form
    global deploymentIsHappening
    global standbyIsHappening
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
        
***FOLLOW THE ADMINISTRATOR IN CHARGE IMMEDIATELY:***''' + "\nhttps://www.roblox.com/users/" + host + "/profile"  + "\n@everyone")
    except:
        print("deployment message error")
    try:
        standbymsg = ('''<:swat:511794129999626270> <:usa:511794381406208000> __**STANDBY ORDER**__ <:usa:511794381406208000> <:swat:511794129999626270>
**DATE: **``''' + timestamp[0] + '''``
**TIME: **``''' + timestamp[1] + " GMT" + '''``
**TYPE: **``''' + threat.upper() + '''``
**LOCATION: **``''' + region.upper() + '''``

ALL UNITS ARE ORDERED TO **STANDBY** FOR POTENTIAL DEPLOYMENT TO THE CITY OF ''' + region.upper() + "." + '''
ALL UNITS SHALL RESPOND WHEN AND IF AN ORDER IS ISSUED WITHIN FIVE (5) MINUTES.''' + "\n@everyone")
    except:
        print("deployment message error")
    if message.content.startswith("!enddeploy"):
        if ((message.author.id == "172128816280371200") or (message.author.id == "259819311735111681")): # ADD ONLY HEAD OF OPERATIONS+ HERE
            if deploymentIsHappening:
                await client.send_message(discord.Object(id='511736808544010275'), "**DEPLOYMENT ENDED AT " + timestamp[1] + " GMT.**")
                await client.send_message(message.channel, "End of deployment has been announced. Remember to log this deployment on the Trello board.")
                deploymentIsHappening = False
            else:
                msg = "There is no deployment to end."
                await client.send_message(message.channel, msg)
        else:
            msg = "You do not have permission to access this command. Contact frostbleed directly for permissions."
            await client.send_message(message.channel, msg)

    if message.content.startswith("!daycare"):
        msg = "\"This is SWAT, not daycare.\" - NCISrox"
        await client.send_message(message.channel, msg)

    if message.content.startswith("!cancelorder"):
        if ((message.author.id == "172128816280371200") or (message.author.id == "259819311735111681")): # ADD ONLY HEAD OF OPERATIONS+ HERE
            if deploymentIsHappening:
                await client.send_message(discord.Object(id='511736808544010275'), "**DEPLOYMENT CANCELLED AT " + timestamp[1] + " GMT.**")
                deploymentIsHappening = False
                await client.send_message(message.channel, "Deployment cancellation has been announced.")
            elif standbyIsHappening:
                await client.send_message(discord.Object(id='511736808544010275'), "**STANDBY CANCELLED AT " + timestamp[1] + " GMT.**")
                standbyIsHappening = False
                await client.send_message(message.channel, "Standby cancellation has been announced.")
            else:
                msg = "There is no deployment to end."
                await client.send_message(message.channel, msg)
        else:
            msg = "You do not have permission to access this command. Contact frostbleed directly for permissions."
            await client.send_message(message.channel, msg)

    if message.content.startswith("!cmds"):
        msg = """**!cmds**: Display a list of commands.
**!deploy**: Issue a deployment order. Format: !deploy <drill/emergency> <lv/dc> <user id>
**!standby**: Issue a standby order. Format: !standby <drill/emergency> <lv/dc>
**!cancelorder**: Announce the cancellation of the last deployment or standby order.
**!enddeploy**: Announce the end of a deployment.
**!delete**: Delete a given number of messages. Format: !delete <integer>"""
        await client.send_message(message.channel, msg)

    if message.content.startswith("!confirm"):
        if ((message.author.id == "172128816280371200") or (message.author.id == "259819311735111681")): # ADD ONLY HEAD OF OPERATIONS+ HERE
            if waitingForConfirmation:
                try:
                    splitreq = (message.content).split(" ")
                    if((splitreq[1] == "drilldeploy") and (threat == "drill") and (form == "deploy")):
                        await client.send_message(discord.Object(id='511736808544010275'), deploymsg)
                        await client.send_message(message.channel, "Deployment announced. Lead with pride and dignity. Good luck.")
                        waitingForConfirmation = False
                        deploymentIsHappening = True
                    elif((splitreq[1] == "emergdeploy") and (threat == "emergency") and (form == "deploy")):
                        await client.send_message(discord.Object(id='511736808544010275'), deploymsg)
                        await client.send_message(message.channel, "Deployment announced. Lead with pride and dignity. Good luck.")
                        waitingForConfirmation = False
                        deploymentIsHappening = True
                    elif((splitreq[1] == "drillstandby") and (threat == "drill") and (form == "standby")):
                        await client.send_message(discord.Object(id='511736808544010275'), standbymsg)
                        await client.send_message(message.channel, "Standby order announced.")
                        waitingForConfirmation = False
                        standbyIsHappening = True
                    elif ((splitreq[1] == "emergstandby") and (threat == "emergency") and (form == "standby")):
                        await client.send_message(discord.Object(id='511736808544010275'), standbymsg)
                        await client.send_message(message.channel,"Standby order announced.")
                        waitingForConfirmation = False
                        standbyIsHappening = True
                    else:
                        msg = "Invalid confirmation."
                        await client.send_message(message.channel, msg)
                except IndexError:
                    msg = "Invalid confirmation."
                    await client.send_message(message.channel, msg)
        else:
            msg = "You do not have permission to access this command. Contact frostbleed directly for permissions."
            await client.send_message(message.channel, msg)

    if message.content.startswith("!standby"):
        if ((message.author.id == "172128816280371200") or (message.author.id == "259819311735111681")): # ADD ONLY HEAD OF OPERATIONS+ HERE
            req = message.content
            splitreq = req.split(" ")
            try:
                if (splitreq[1] == "drill"):
                    if(splitreq[2] == "lv"):
                        form = "standby"
                        threat = "drill"
                        region = "las vegas"
                        waitingForConfirmation = True
                        msg = "**READ CAREFULLY AND CONFIRM WITH !confirm drillstandby**:\n``DRILL DEPLOYMENT STANDBY REQUEST TO LAS VEGAS``" + "\n\n**ENSURE YOU ARE AT LAS VEGAS PRIOR TO CONFIRMING**\n**IF INCORRECT, RETYPE STANDBY COMMAND**"
                    elif(splitreq[2] == "dc"):
                        form = "standby"
                        threat = "drill"
                        region = "washington dc"
                        waitingForConfirmation = True
                        msg = "**READ CAREFULLY AND CONFIRM WITH !confirm drillstandby**:\n``DRILL DEPLOYMENT STANDBY REQUEST TO WASHINGTON DC``" + "\n\n**ENSURE YOU ARE AT WASHINGTON DC PRIOR TO CONFIRMING**\n**IF INCORRECT, RETYPE STANDBY COMMAND**"
                    else:
                        msg = "Invalid deployment request. Format: !deploy <drill/emergency> <lv/dc> <id>"
                elif (splitreq[1] == "emergency"):
                    if(splitreq[2] == "lv"):
                        form = "standby"
                        threat = "emergency"
                        region = "las vegas"
                        waitingForConfirmation = True
                        msg = "**READ CAREFULLY AND CONFIRM WITH !confirm emergstandby**:\n``EMERGENCY DEPLOYMENT STANDBY REQUEST TO LAS VEGAS``" + "\n\n**ENSURE YOU ARE AT LAS VEGAS PRIOR TO CONFIRMING**\n**IF INCORRECT, RETYPE STANDBY COMMAND**"
                    elif(splitreq[2] == "dc"):
                        form = "standby"
                        threat = "emergency"
                        region = "washington dc"
                        waitingForConfirmation = True
                        msg = "**READ CAREFULLY AND CONFIRM WITH !confirm emergstandby**:\n``EMERGENCY DEPLOYMENT STANDBY REQUEST TO WASHINGTON DC``" + "\n\n**ENSURE YOU ARE AT WASHINGTON DC PRIOR TO CONFIRMING**\n**IF INCORRECT, RETYPE STANDBY COMMAND**"
                    else:
                        msg = "Invalid standby request. Format: !standby <drill/emergency> <lv/dc>"
                else:
                    msg = "Invalid standby request. Format: !standby <drill/emergency> <lv/dc>"
            except IndexError:
                msg = "Invalid standby request. Format: !standby <drill/emergency> <lv/dc>"
        else:
            msg = "You do not have permission to access this command. Contact frostbleed directly for permissions."
        await client.send_message(message.channel, msg)

    if message.content.startswith("!deploy"):
        if ((message.author.id == "172128816280371200") or (message.author.id == "259819311735111681")): # ADD ONLY HEAD OF OPERATIONS+ HERE
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
        else:
            msg = "You do not have permission to access this command. Contact frostbleed directly for permissions."
        await client.send_message(message.channel, msg)
        
@client.command(pass_context = True)
async def delete(ctx, amount):
    if ((ctx.message.author.id == "172128816280371200") or (ctx.message.author.id == "259819311735111681")):  # ADD ONLY LIEUTENANT+ HERE
        try:
            channel = ctx.message.channel
            todel = []
            async for message in client.logs_from(channel, limit=int(amount) + 1):
                todel.append(message)
            await client.delete_messages(todel)
            await client.send_message(ctx.message.channel, (amount + " messages deleted."))
        except:
            await client.send_message(ctx.message.channel, "Deletion error: You must indicate a range of 2 to 100 messages to delete, and no messages may be over 2 weeks old.")
    else:
        await client.send_message(ctx.message.channel, "You do not have permission to access this command. Contact frostbleed directly for permissions.")
        
client.run(os.getenv('TOKEN'))
