import os
import discord
import os
from keep_alive import keep_alive
import random
import asyncio
import aiohttp
import json

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='?')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} bork!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hei {member.name}, Voff!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    quotes = [
        ':dog:' ,
        ':smirk:',
        (
            'Cool. Cool cool cool'
        ),
    ]
    
    if message.content == 'cool':
        response = random.choice(quotes)
        await message.channel.send(response)

@bot.command(name='terning_kast', help='Simulerer terningkast.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

keep_alive()
client.run(TOKEN)