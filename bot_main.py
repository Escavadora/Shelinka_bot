# https://github.com/Escavadora/Shelinka_bot
# TODO add description='Unicorn Petting Zoo 2019' somewhere

import discord
import asyncio
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot

# Comment this line if you want to test
# tokenFile = open('token.txt', 'r')

# Comment this line if you want to deploy
tokenFile = open('token2.txt', 'r')

BOT_PREFIX = ('!', '?')
TOKEN = tokenFile.read()
client = Bot(command_prefix=BOT_PREFIX)

def __init__(self, client):
    self.client = client


async def isSecretUser(ctx):
    return ctx.author.id == 204287692542836736


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.listen()
async def reactMessage(message):
    if message.channel == client.get_channel('468781121497333762'):
        emoji1 = get(client.get_all_emojis(), name='Ready')
        emoji2 = get(client.get_all_emojis(), name='NotReady')
        await message.add_reaction(emoji1)
        await message.add_reaction(emoji2)


@client.command()
@commands.cooldown(1, 60, commands.BucketType.server)
async def faq():
    # emojibirb = get(bot.get_all_emojis(), name='CuteBirb')
    msg = 'Hey there :wave: , please read #roles and #faq , you will find almost everything there. ' \
          'If you have any other questions feel free to ask <:CuteBirb:454812443752005632> '
    await client.say(msg)

'''@bot.command()
@commands.check(isSecretUser)
async def shelinka():
    if message.author.id != '204287692542836736':
        return
    msg = 'https://i.imgur.com/Q4PtRPr.jpg'.format(message)
    await bot.say(msg)'''

'''@bot.command()
async def list():
    bot.say("Starting to look for wrong roles")
    mem = message.server.members
    acceptableroles = ["High Warlord", "Scout", "Centurion", "Spellwing Champion", "Peon", "Event General"]
    for member in mem:
        if not any((x.name in acceptableroles) for x in member.roles):
            await client.send_message(message.channel, member.mention)
    await client.send_message(message.channel, "Done looking for wrong roles")'''


client.run(TOKEN)
