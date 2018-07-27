# https://github.com/Escavadora/Shelinka_bot
# TODO reroll

from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Game
import datetime
import discord

# Comment this line if you want to test
# tokenFile = open('token.txt', 'r')

# Comment this line if you want to deploy
tokenFile = open('token2.txt', 'r')

BOT_PREFIX = ('!', '?')
TOKEN = tokenFile.read()
client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Unicorn Petting Zoo 2019'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.channel.id == '468781121497333762':
        emoji1 = get(client.get_all_emojis(), name='Ready')
        emoji2 = get(client.get_all_emojis(), name='NotReady')
        await client.add_reaction(message, emoji1)
        await client.add_reaction(message, emoji2)
    await client.process_commands(message)


@client.command(description='Posts response leading people to #faq and #roles')
@commands.cooldown(1, 60, commands.BucketType.server)
async def faq():
    msg = 'Hey there :wave: , please read #roles and #faq , you will find almost everything there. ' \
          'If you have any other questions feel free to ask <:CuteBirb:454812443752005632> '
    await client.say(msg)


@client.command(brief='Meme ?',
                aliases=['Shelinka'],
                pass_context=True)
@commands.cooldown(1, 300, commands.BucketType.server)
async def shelinka(ctx):
    if ctx.message.author.id != '204287692542836736':
        return
    else:
        msg = 'https://i.imgur.com/Q4PtRPr.jpg'
        await client.say(msg)


'''@client.command(brief='Raffle command',
                description='Use command in format !raffle <raffle name> <channel> <duration> <number of winners>',
                pass_context=True)
async def raffle(mesg, channel, duration, winner_num, *, name):
    embed = discord.Embed(
        title=name,
        description=f'React with :tada: to win!',
        color=discord.Color.magenta(),
        #timestamp='19:10'
    )
    #embed.set_footer(text='Ends at')
    msg = await channel.send(embed=embed)
    await msg.add_reaction(':tada:')'''
'''msg = ':point_right: **GIVEAWAY** :point_left:\n*{}*\n**{} WINNERS** \nReact with :tada: to enter!' \
            '\nDuration: {} seconds\nEnds at: {}'.format(name, winner_num, duration, channel)
    await client.say(msg)
    await client.add_reaction(msg, 'tada')'''

'''@bot.command(pass_context=True)
async def list():
    client.say("Starting to look for wrong roles")
    mem = message.server.members
    acceptableroles = ["High Warlord", "Scout", "Centurion", "Spellwing Champion", "Peon", "Event General"]
    for member in mem:
        if not any((x.name in acceptableroles) for x in member.roles):
            await client.send_message(message.channel, member.mention)
    await client.say(message.channel, "Done looking for wrong roles")'''


client.run(TOKEN)
