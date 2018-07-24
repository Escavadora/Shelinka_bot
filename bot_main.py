# https://github.com/Escavadora/Shelinka_bot
# TODO regex for FAQ

import discord
import asyncio
from discord.utils import get
from discord.ext import commands

tokenFile = open('token.txt', 'r')
TOKEN = tokenFile.read()
bot = commands.Bot(command_prefix='!', description='Unicorn Petting Zoo 2019')

async def isSecretUser(ctx):
    return ctx.author.id == 204287692542836736

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.listen()
async def reactMessage(message):
    if message.channel == client.get_channel('468781121497333762'):
        emoji1 = get(client.get_all_emojis(), name='Ready')
        emoji2 = get(client.get_all_emojis(), name='NotReady')
        await message.add_reaction(emoji1)
        await message.add_reaction(emoji2)


@bot.command()
async def faq(ctx, arg):
    emojibirb = get(bot.get_all_emojis(), name='CuteBirb')
    msg = 'Hey there :wave: , please read #roles and #faq , you will find almost everything there. If you have any other questions feel free to ask {} '.format(emojibirb)
    await bot.say(msg)

@bot.command()
@commands.check(isSecretUser)
async def shelinka():
    if message.author.id != '204287692542836736':
        return
    msg = 'https://i.imgur.com/Q4PtRPr.jpg'.format(message)
    await bot.say(msg)

@bot.command()
async def list():
    bot.say("Starting to look for wrong roles")
    mem = message.server.members
    acceptableroles = ["High Warlord", "Scout", "Centurion", "Spellwing Champion", "Peon", "Event General"]
    for member in mem:
        if not any((x.name in acceptableroles) for x in member.roles):
            await client.send_message(message.channel, member.mention)
    await client.send_message(message.channel, "Done looking for wrong roles")


client.run(TOKEN)
