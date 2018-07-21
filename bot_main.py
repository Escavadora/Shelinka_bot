# https://github.com/Escavadora/Shelinka_bot
# TODO regex for FAQ

import discord
from discord.utils import get

tokenFile = open('token.txt', 'r')
TOKEN = tokenFile.read()

client = discord.Client()

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!faq'):
        msg = 'Hey there :wave: , please read #roles and #faq , you will find almost everything there. If you have any other questions feel free to ask <:CuteBirb:454812443752005632> '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!shelinka'):
        if message.author.id == ('204287692542836736'):
            msg = 'https://i.imgur.com/Q4PtRPr.jpg'.format(message)
            await client.send_message(message.channel, msg)

    if message.content.startswith(''):
        if message.channel == client.get_channel('468781121497333762'):
            emoji1 = get(client.get_all_emojis(), name='Ready')
            emoji2 = get(client.get_all_emojis(), name='NotReady')
            await client.add_reaction(message, emoji1)
            await client.add_reaction(message, emoji2)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='Unicorn Petting Zoo 2019'))

client.run(TOKEN)
