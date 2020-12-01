import discord
import random
import numpy as np

from discord.ext import commands


participants = []
client = commands.Bot( command_prefix = '.')


@client.event
async def on_ready():
        print('bot is ready')


@client.event
async def on_member_join(member):
        print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
        print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
        await ctx.send('Pong!')

@client.command()
async def register(ctx):
        await ctx.send("name? : ")

        def check(msg):
                return msg.author == ctx.author and msg.channel == ctx.channel
        responses = []
        msg = await client.wait_for("message", check=check)
        responses.append(msg.content)
        await ctx.send("email? : ")
        msg = await client.wait_for("message", check=check)
        responses.append(msg.content)
        await ctx.send("address? : ")
        msg = await client.wait_for("message", check=check)
        responses.append(msg.content)
        responses.append(msg.author)
        await ctx.send("You have been registered")



        participants.append(participant(responses[0],responses[1],responses[2],responses[3]))

@client.command()
async def shufflesend(ctx):
        await ctx.send("You sure you want to shufflesend?")
        def check(msg):
                return msg.author == ctx.author and msg.channel == ctx.channel

        msg = await client.wait_for("message", check=check)
        if (msg.content == "shufflesend"):
                if (len(participants) % 2 ==0):
                        random.shuffle(participants)

#                       sendmail(participants)
                        await ctx.send("done")
                else:
                        await ctx.send("there is an odd number of participants. try again later.")



@client.command()
async def lp(ctx):
        for x in range(len(participants)):
                await ctx.send(participants[x].__dict__)


def sendmail(list):
        for person in list:
                print ('sent ', person.name, ' a message')

def pair(list):
        merged_list = []
        half = np.array_split(list, (len(list)/2))
        merged_list = tuple(zip(list, half))
        for pairing in merged_list:
                print(pairing)
        return merged_list


class participant:
        def __init__(self, name, email, address, id):
                self.name = name
                self.email = email
                self.address = address
                self.id = id

