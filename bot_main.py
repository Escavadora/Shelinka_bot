# https://github.com/Escavadora/Shelinka_bot
# TODO regex for FAQ
# TODO purge command only available to admins

import discord

tokenFile = open('token.txt', 'r')
TOKEN = tokenFile.read()

client = discord.Client()

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hey there {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!faq'):
        msg = 'Hey there :wave: , please read #roles and #faq , you will find almost everything there. If you have any other questions feel free to ask :CuteBirb: '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!shelinka'):
        if message.author.id == ('204287692542836736'):
            msg = 'https://i.imgur.com/Q4PtRPr.jpg'.format(message)
            await client.send_message(message.channel, msg)

    if message.content.startswith('!athena'):
        if message.author.id == ('210113891248766976'):
            msg = 'https://i.imgur.com/O6lkJZH.png'.format(message)
            await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='Sending nudes to Treebo'))

client.run(TOKEN)
