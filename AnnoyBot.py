import discord # Make sure you have discord.py installed!
import asyncio

# Made By: Digital Disarray
# Purpose of this bot is to automatically delete messages from someone that you don't like.

client = discord.Client()

error = '[ ERROR ] - '
warn =  '[ WARN ] -'
info =  '[ INFO ] - '

@client.event
async def on_ready():
    print(info + 'Logged In!')
    print('Username: ' + client.user.name)
    print('User ID: ' + client.user.id)
    print('=====================')


@client.event
async def on_message(message):
    if str(message.author) == 'target#XXXX':
        print(info + 'Message from ' + str(message.author) + ' deleted. Text: ' + str(message.content))
        await client.delete_message(message)

client.run('ENTER TOKEN HERE') # Make sure you have added your own token!
