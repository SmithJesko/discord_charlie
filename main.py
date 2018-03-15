import discord
from discord.ext.commands import Bot
import secrets
from cleverwrap import CleverWrap
import random

bot = Bot(command_prefix = "$")
cw = CleverWrap(secrets.cleverbot_key)

@bot.event
async def on_ready():
    print("Ready!")
    print("Logged in as: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print("discord.py v{}".format(discord.__version__))

@bot.command()
async def say(*args):
    # print(args)
    # print(' '.join(args))
    message = ' '.join(args)
    reply = cw.say(message)
    return await bot.say(reply)

@bot.command()
async def flip(*args):
    flip = random.choice(['Heads', 'Tails'])
    return await bot.say(flip)

@bot.event
async def on_message(message):
    print(message.author, message.content)

bot.run(secrets.discord_key)