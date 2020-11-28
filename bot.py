import discord
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
	await ctx.send("You have been registered")



	participants.append(participant(responses[0],responses[1],responses[2]))
	print(f'{participants}')

@client.command()
async def shufflesend(ctx):
	await ctx.send("You sure you want to shufflesend?")
	def check(msg):
		return msg.author == ctx.author and msg.channel == ctx.channel 
	
	msg = await client.wait_for("message", check=check)
	if (msg.content == "shufflesend"):
		sendmail(participants)
		await ctx.send("Done")



def sendmail(list):
	for person in list:
		print ('sent ', person.name, ' a message')

class participant:
	def __init__(self, name, email, address):
		self.name = name
		self.email = email
		self.address = address





















client.run('NzgyMzA3NjExMzM2NTA3NDAy.X8KSvQ.ydNxaKGbV3WWbsNj9NwtQKBI2ag')
