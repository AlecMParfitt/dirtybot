# bot.py
import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client(intents=discord.Intents.default())
intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def roll(ctx, arg):
    """Rolls a dice in NdN format. Usage: !roll [number of dice]d[number of sides]"""
    if arg == 'help':
        await ctx.send('Usage: !roll [number of dice]d[number of sides]')
        return
    if 'd' not in arg:
        await ctx.send('Usage: !roll [number of dice]d[number of sides]')
        return

    dice_num, dice_type = arg.split('d')
    if dice_num == '':
        dice_num = 1
    else:
        dice_num = int(dice_num)
    dice_type = int(dice_type)
    dice = [str(random.choice(range(1, dice_type + 1))) for _ in range(dice_num)]
    await ctx.send("Rolling " + str(dice_num) + "d" + str(dice_type) + "...")
    sum = 0
    for die in dice:
        sum += int(die)
    await ctx.send(', '.join(dice))
    await ctx.send(" Dice total: " + str(sum))



client.run(TOKEN)
