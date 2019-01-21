import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import datetime
import random

Client = discord.Client()
client = commands.Bot(command_prefix="!")


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
requester = 13231


@client.event
async def on_message(message):
    global waitingForConfirmation
    global threat
    global region
    global host
    global requester
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

***FOLLOW THE ADMINISTRATOR IN CHARGE IMMEDIATELY:***''' + "\nhttps://www.roblox.com/users/" + host + "/profile" + "\n@everyone")
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
    if ((message.content).lower()).startswith("!enddeploy"):
        if ((message.author.id == "172128816280371200") or (
                message.author.id == "259819311735111681") or (
                message.author.id == "535577946526842883") or (
                message.author.id == "417606473947021312") or (
                message.author.id == "220553967627796480") or (
                message.author.id == "249181931281842186")):  # ADD ONLY HEAD OF OPERATIONS+ HERE
            if deploymentIsHappening:
                await client.send_message(discord.Object(id='511736808544010275'),
                                          "**DEPLOYMENT ENDED AT " + timestamp[1] + " GMT.**")
                await client.send_message(message.channel,
                                          "End of deployment has been announced. Remember to log this deployment on the Trello board.")
                deploymentIsHappening = False
            else:
                msg = "There is no deployment to end."
                await client.send_message(message.channel, msg)
        else:
            msg = "You do not have permission to access this command. Contact frostbleed directly for permissions."
            await client.send_message(message.channel, msg)

    if ((message.content).lower()).startswith("!daycare"):
        msg = "\"This is SWAT, not daycare.\" - NCISrox"
        await client.send_message(message.channel, msg)
        
    if ((message.content).lower()).startswith("frost"):
        msg = "*Sir"
        await client.send_message(message.channel, msg)
        
    if ((message.content).lower()).startswith("epic"):
        msg = "Ben Shapiro epic gamer moment"
        await client.send_message(message.channel, msg)

    if ((message.content).lower()).startswith("snow"):
        msg = "*Hon. President pro tempore snowbleed"
        await client.send_message(message.channel, msg)
        
    if ((message.content).lower()).startswith("kyle"):
        msg = "*KYLELUONG2004"
        await client.send_message(message.channel, msg)
        
    if ((message.content).lower()).startswith("!delete"):
        if ((message.author.id == "172128816280371200") or (
                message.author.id == "259819311735111681") or (
                message.author.id == "535577946526842883") or (
                message.author.id == "417606473947021312") or (
                message.author.id == "220553967627796480") or (
                message.author.id == "249181931281842186")):  # ADD ONLY LIEUTENANT+ HERE
            try:
                text = (message.content).split(" ")
                channel = message.channel
                todel = []
                async for message in client.logs_from(channel, limit=(int(text[1]) + 1)):
                    todel.append(message)
                await client.delete_messages(todel)
                rtrn = text[1] + " messages deleted."
                await client.send_message(message.channel, rtrn)
            except:
                await client.send_message(message.channel,
                                          "Deletion error: You must indicate a range of 2 to 100 messages to delete, and no messages may be over 2 weeks old.")
        else:
            await client.send_message(message.channel,
                                      "You do not have permission to access this command. Contact frostbleed directly for permissions.")

    if ((message.content).lower()).startswith("!cancelorder"):
        if ((message.author.id == "172128816280371200") or (
                message.author.id == "259819311735111681") or (
                message.author.id == "535577946526842883") or (
                message.author.id == "417606473947021312") or (
                message.author.id == "220553967627796480") or (
                message.author.id == "249181931281842186")):  # ADD ONLY HEAD OF OPERATIONS+ HERE
            if deploymentIsHappening:
                await client.send_message(discord.Object(id='511736808544010275'),
                                          "**DEPLOYMENT CANCELLED AT " + timestamp[1] + " GMT.**")
                deploymentIsHappening = False
                await client.send_message(message.channel, "Deployment cancellation has been announced.")
            elif standbyIsHappening:
                await client.send_message(discord.Object(id='511736808544010275'),
                                          "**STANDBY CANCELLED AT " + timestamp[1] + " GMT.**")
                standbyIsHappening = False
                await client.send_message(message.channel, "Standby cancellation has been announced.")
            else:
                msg = "There is no deployment to end."
                await client.send_message(message.channel, msg)
        else:
            msg = "You do not have permission to access this command. Contact frostbleed directly for permissions."
            await client.send_message(message.channel, msg)

    if ((message.content).lower()).startswith("!cmds"):
        msg = """**!cmds**: Display a list of commands.
**!deploy**: Issue a deployment order. Format: !deploy <drill/emergency> <lv/dc> <user id>
**!standby**: Issue a standby order. Format: !standby <drill/emergency> <lv/dc>
**!cancelorder**: Announce the cancellation of the last deployment or standby order.
**!enddeploy**: Announce the end of a deployment.
**!delete**: Delete a given number of messages. Format: !delete <integer>
**!rps**: Play a game of rock-paper-scissors. Format: !rps <rock/paper/scissors>
**!8ball**: Ask a question, and say !8ball for the RSO's opinion."""
        await client.send_message(message.channel, msg)

    if ((message.content).lower()).startswith("!8ball"):
        choice = random.randint(1,11)
        if choice == 1:
            msg = "🎱 I don't know."
        elif choice == 2:
            msg = "🎱 I couldn't care less."
        elif choice == 3:
            msg = "🎱 100% absolutely."
        elif choice == 4:
            msg = "🎱 Yes."
        elif choice == 5:
            msg = "🎱 Of course. Isn't it obvious?"
        elif choice == 6:
            msg = "🎱 Certainly."
        elif choice == 7:
            msg = "🎱 Negative."
        elif choice == 8:
            msg = "🎱 Nope."
        elif choice == 9:
            msg = "🎱 Of course not."
        elif choice == 10:
            msg = "🎱 Never."
        else:
            msg = "🎱 Never."
        await client.send_message(message.channel, msg)

    if ((message.content).lower()).startswith("!rps"):
        pickanumber = random.randint(1, 4)
        if pickanumber == 1:
            play = "rock"
        elif pickanumber == 2:
            play = "scissors"
        elif pickanumber == 3:
            play = "paper"
        else:
            play = "rock"
        msgval = ((message.content).lower()).split(" ")
        try:
            if(msgval[1] == "rock"):
                if play == "rock":
                    msg = "RSO plays rock. Tie!"
                elif play == "scissors":
                    msg = "RSO plays scissors. You win!"
                elif play == "paper":
                    msg = "RSO plays paper. You lose!"
                else:
                    msg = "Invalid rock-paper-scissors command. Format: !rps <rock/paper/scissors>"
            elif(msgval[1] == "paper"):
                if play == "rock":
                    msg = "RSO plays rock. You win!"
                elif play == "scissors":
                    msg = "RSO plays scissors. You lose!"
                elif play == "paper":
                    msg = "RSO plays paper. Tie!"
                else:
                    msg = "Invalid rock-paper-scissors command. Format: !rps <rock/paper/scissors>"
            elif (msgval[1] == "scissors"):
                if play == "rock":
                    msg = "RSO plays rock. You lose!"
                elif play == "scissors":
                    msg = "RSO plays scissors. Tie!"
                elif play == "paper":
                    msg = "RSO plays paper. You win!"
                else:
                    msg = "Invalid rock-paper-scissors command. Format: !rps <rock/paper/scissors>"
            else:
                msg = "Invalid rock-paper-scissors command. Format: !rps <rock/paper/scissors>"
        except:
            msg = "Invalid rock-paper-scissors command. Format: !rps <rock/paper/scissors>"
        await client.send_message(message.channel, msg)

    if ((message.content).lower()).startswith("!cancel"):
        if ((message.author.id == "172128816280371200") or (
                message.author.id == "259819311735111681") or (
                message.author.id == "535577946526842883") or (
                message.author.id == "220553967627796480") or (
                message.author.id == "249181931281842186")):  # ADD ONLY HEAD OF OPERATIONS+ HERE
            if(waitingForConfirmation):
                waitingForConfirmation = False
                msg = "**CANCELLATION CONFIRMED**"
            else:
                msg = "No orders to cancel."
        else:
            msg = "You do not have permission to access this command. Contact frostbleed directly for permissions."
        await client.send_message(message.channel, msg)
            
    if ((message.content).lower()).startswith("!confirm"):
        if (message.author.id == requester):
            if waitingForConfirmation:
                try:
                    splitreq = (message.content).split(" ")
                    if ((splitreq[1] == "drilldeploy") and (threat == "drill") and (form == "deploy")):
                        await client.send_message(discord.Object(id='511736808544010275'), deploymsg)
                        await client.send_message(message.channel,
                                                  "Deployment announced. Lead with pride and dignity. Good luck.")
                        waitingForConfirmation = False
                        deploymentIsHappening = True
                    elif ((splitreq[1] == "emergdeploy") and (threat == "emergency") and (form == "deploy")):
                        await client.send_message(discord.Object(id='511736808544010275'), deploymsg)
                        await client.send_message(message.channel,
                                                  "Deployment announced. Lead with pride and dignity. Good luck.")
                        waitingForConfirmation = False
                        deploymentIsHappening = True
                    elif ((splitreq[1] == "drillstandby") and (threat == "drill") and (form == "standby")):
                        await client.send_message(discord.Object(id='511736808544010275'), standbymsg)
                        await client.send_message(message.channel, "Standby order announced.")
                        waitingForConfirmation = False
                        standbyIsHappening = True
                    elif ((splitreq[1] == "emergstandby") and (threat == "emergency") and (form == "standby")):
                        await client.send_message(discord.Object(id='511736808544010275'), standbymsg)
                        await client.send_message(message.channel, "Standby order announced.")
                        waitingForConfirmation = False
                        standbyIsHappening = True
                    else:
                        msg = "Invalid confirmation."
                        await client.send_message(message.channel, msg)
                except IndexError:
                    msg = "Invalid confirmation."
                    await client.send_message(message.channel, msg)
        else:
            msg = "Only the requester may confirm an order."
            await client.send_message(message.channel, msg)

    if ((message.content).lower()).startswith("!standby"):
        if ((message.author.id == "172128816280371200") or (
                message.author.id == "259819311735111681") or (
                message.author.id == "535577946526842883") or (
                message.author.id == "417606473947021312") or (
                message.author.id == "220553967627796480") or (
                message.author.id == "249181931281842186")):  # ADD ONLY HEAD OF OPERATIONS+ HERE
            req = (message.content).lower()
            splitreq = req.split(" ")
            try:
                if (splitreq[1] == "drill"):
                    if (splitreq[2] == "lv"):
                        form = "standby"
                        threat = "drill"
                        region = "las vegas"
                        waitingForConfirmation = True
                        requester = message.author.id
                        msg = "**READ CAREFULLY AND CONFIRM WITH !confirm drillstandby**:\n``DRILL DEPLOYMENT STANDBY REQUEST TO LAS VEGAS``" + "\n\n**ENSURE YOU ARE AT LAS VEGAS PRIOR TO CONFIRMING**\n**IF INCORRECT, TYPE !cancel**"
                    elif (splitreq[2] == "dc"):
                        form = "standby"
                        threat = "drill"
                        region = "washington dc"
                        waitingForConfirmation = True
                        requester = message.author.id
                        msg = "**READ CAREFULLY AND CONFIRM WITH !confirm drillstandby**:\n``DRILL DEPLOYMENT STANDBY REQUEST TO WASHINGTON DC``" + "\n\n**ENSURE YOU ARE AT WASHINGTON DC PRIOR TO CONFIRMING**\n**IF INCORRECT, TYPE !cancel**"
                    else:
                        msg = "Invalid deployment request. Format: !deploy <drill/emergency> <lv/dc> <id>"
                elif (splitreq[1] == "emergency"):
                    if (splitreq[2] == "lv"):
                        form = "standby"
                        threat = "emergency"
                        region = "las vegas"
                        waitingForConfirmation = True
                        requester = message.author.id
                        msg = "**READ CAREFULLY AND CONFIRM WITH !confirm emergstandby**:\n``EMERGENCY DEPLOYMENT STANDBY REQUEST TO LAS VEGAS``" + "\n\n**ENSURE YOU ARE AT LAS VEGAS PRIOR TO CONFIRMING**\n**IF INCORRECT, TYPE !cancel**"
                    elif (splitreq[2] == "dc"):
                        form = "standby"
                        threat = "emergency"
                        region = "washington dc"
                        waitingForConfirmation = True
                        requester = message.author.id
                        msg = "**READ CAREFULLY AND CONFIRM WITH !confirm emergstandby**:\n``EMERGENCY DEPLOYMENT STANDBY REQUEST TO WASHINGTON DC``" + "\n\n**ENSURE YOU ARE AT WASHINGTON DC PRIOR TO CONFIRMING**\n**IF INCORRECT, TYPE !cancel**"
                    else:
                        msg = "Invalid standby request. Format: !standby <drill/emergency> <lv/dc>"
                else:
                    msg = "Invalid standby request. Format: !standby <drill/emergency> <lv/dc>"
            except IndexError:
                msg = "Invalid standby request. Format: !standby <drill/emergency> <lv/dc>"
        else:
            msg = "You do not have permission to access this command. Contact frostbleed directly for permissions."
        await client.send_message(message.channel, msg)

    if ((message.content).lower()).startswith("!deploy"):
        if ((message.author.id == "172128816280371200") or (
                message.author.id == "259819311735111681") or (
                message.author.id == "535577946526842883") or (
                message.author.id == "417606473947021312") or (
                message.author.id == "220553967627796480") or (
                message.author.id == "249181931281842186")):  # ADD ONLY HEAD OF OPERATIONS+ HERE
            req = (message.content).lower()
            splitreq = req.split(" ")
            try:
                if (splitreq[1] == "drill"):
                    if (splitreq[2] == "lv"):
                        form = "deploy"
                        threat = "drill"
                        region = "las vegas"
                        host = splitreq[3]
                        waitingForConfirmation = True
                        requester = message.author.id
                        msg = "**READ CAREFULLY AND CONFIRM WITH !confirm drilldeploy**:\n``DRILL DEPLOYMENT REQUEST TO LAS VEGAS, HOSTED BY " + \
                              splitreq[
                                  3] + "``" + "\n\n**ENSURE YOU ARE AT LAS VEGAS PRIOR TO CONFIRMING**\n**IF INCORRECT, TYPE !cancel**"
                    elif (splitreq[2] == "dc"):
                        form = "deploy"
                        threat = "drill"
                        region = "washington dc"
                        host = splitreq[3]
                        waitingForConfirmation = True
                        requester = message.author.id
                        msg = "**READ CAREFULLY AND CONFIRM WITH !confirm drilldeploy**:\n``DRILL DEPLOYMENT REQUEST TO WASHINGTON DC, HOSTED BY " + \
                              splitreq[
                                  3] + "``" + "\n\n**ENSURE YOU ARE AT WASHINGTON DC PRIOR TO CONFIRMING**\n**IF INCORRECT, TYPE !cancel**"
                    else:
                        msg = "Invalid deployment request. Format: !deploy <drill/emergency> <lv/dc> <id>"
                elif (splitreq[1] == "emergency"):
                    if (splitreq[2] == "lv"):
                        form = "deploy"
                        threat = "emergency"
                        region = "las vegas"
                        host = splitreq[3]
                        waitingForConfirmation = True
                        requester = message.author.id
                        msg = "**READ CAREFULLY AND CONFIRM WITH !confirm emergdeploy**:\n``EMERGENCY DEPLOYMENT REQUEST TO LAS VEGAS, HOSTED BY " + \
                              splitreq[
                                  3] + "``" + "\n\n**ENSURE YOU ARE AT LAS VEGAS PRIOR TO CONFIRMING**\n**IF INCORRECT, TYPE !cancel**"
                    elif (splitreq[2] == "dc"):
                        form = "deploy"
                        threat = "emergency"
                        region = "washington dc"
                        host = splitreq[3]
                        waitingForConfirmation = True
                        requester = message.author.id
                        msg = "**READ CAREFULLY AND CONFIRM WITH !confirm emergdeploy**:\n``EMERGENCY DEPLOYMENT REQUEST TO WASHINGTON DC, HOSTED BY " + \
                              splitreq[
                                  3] + "``" + "\n\n**ENSURE YOU ARE AT WASHINGTON DC PRIOR TO CONFIRMING**\n**IF INCORRECT, TYPE !cancel**"
                    else:
                        msg = "Invalid deployment request. Format: !deploy <drill/emergency> <lv/dc> <user id>"
                else:
                    msg = "Invalid deployment request. Format: !deploy <drill/emergency> <lv/dc> <user id>"
            except IndexError:
                msg = "Invalid deployment request. Format: !deploy <drill/emergency> <lv/dc> <user id>"
        else:
            msg = "You do not have permission to access this command. Contact frostbleed directly for permissions."
        await client.send_message(message.channel, msg)


client.run(os.getenv('TOKEN'))
