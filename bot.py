import discord
import random
import numpy as np
from discord.ext import commands


participants = []

client = commands.Bot( command_prefix = '.')


@client.event
async def on_ready():
        print('bot is ready')


@client.command()
async def register(ctx):
        responses = []
        await ctx.send("name? : ")

        def check(msg):
                return msg.author == ctx.author and msg.channel == ctx.channel

        msg = await client.wait_for("message", check=check)
        responses.append(msg.content)
        await ctx.send("email? : ")
        msg = await client.wait_for("message", check=check)
        responses.append(msg.content)
        await ctx.send("address? : ")
        msg = await client.wait_for("message", check=check)
        responses.append(msg.content)
        await ctx.send("notes? : ")
        msg = await client.wait_for("message", check=check)
        responses.append(msg.content)
        responses.append(msg.author)
        await ctx.send("You have been registered")
        participants.append(participant(responses[0],responses[1],responses[2],responses[3],responses[4]))

@client.command()
async def shufflesend(ctx):
        await ctx.send("You sure you want to shufflesend?")
        def check(msg):
                return msg.author == ctx.author and msg.channel == ctx.channel

        msg = await client.wait_for("message", check=check)
        if (msg.content == "shufflesend"):
                if (len(participants) % 2 ==0):
                        random.shuffle(participants)
                        await sendmail()
                        await ctx.send("done")
                else:
                        await ctx.send("there is an odd number of participants. try again later.")


@client.command()
async def lp(ctx):
        for x in range(len(participants)):
                await ctx.send(participants[x].__dict__)

@client.command()
async def clear(ctx):
        participants.clear()
        await ctx.send("cleared array")



class participant:
        def __init__(self, name, email, address, notes, id):
                self.name = name
                self.email = email
                self.address = address
                self.notes = notes
                self.id = id

async def sendmail():
        for x in range(len(participants)):
                if(x != len(participants)-1):
                        user_disc = client.get_user(participants[x].id.id)
                        user = (participants[x])
                        next = (participants[x+1])
                        output = ('Hello ' + user.id.name + '\n You got paried with ' + next.id.name + '\n here is their info: ' + '\n IRL Name: '+ next.name + '\n Email : ' + next.email + '\n Address : ' + next.address + '\n Notes : ' + next.notes)
                        await user_disc.send(output)


                else:
                        user_disc = client.get_user(participants[x].id.id)
                        user = (participants[x])
                        first = (participants[0])
                        output = ('Hello ' + user.id.name  + '\n You got paried with ' + first.id.name + '\n here is their info:  ' + '\n IRL Name: '+ first.name + '\n Email : ' + first.email + '\n Address : ' + first.address + '\n Notes : ' + first.notes)
                        await user_disc.send(output)
