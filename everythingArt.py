import discord
from discord.ext import commands
from discord.commands import Option
import config
import os

import random

bot = commands.Bot(case_insensitive=True)
thumbnails = config.thumbnails
sketch_ideas = config.sketch_ideas
thumbnail = [f for f in os.listdir(config.thumbnails)]


@bot.event
async def on_ready():
    print("%s is online!" % bot.user.name)
""" 

for f in os.listdir("c:/Users/17062/Documents/New folder/test/"):
    print(f) """

""" art_ideasTemp = ['ICE CREAM', 'Finis Strawbeary', 'KITTY', 'FRUIT', 'GHOST', 'SEASON', 'ILLUMINATE', 'ORIGAMI', 'WATERFALL', 'CASTLE', 'GAMING', 'NINETIES', 'UNDER THE SEA', 'JOURNEY', 'ZODIAC',
             'DONUT', 'FAIRYTALE', 'MOUNTAINS', 'COZY', 'JUNGLE', 'SOUR', 'CAMPING', 'DESERT', 'INTERGALACTIC', 'CELEBRATE', 'PRESENT', 'KAWAII', 'VEGGIES', 'TREASURE', 'SUMMER  DAY', 'ZOMBIE', 'FLOWERS']
 """
data = open(f'{config.art_ideas}', 'r')
art_ideas = data.read().split('\n')
#print(data)

@bot.slash_command(guild_ids=config.guilds, description="Art Idea")
async def idea(ctx):
    await ctx.response.defer()
    idx = random.randint(0, len(art_ideas)-1)
    idx2 = random.randint(0, len(thumbnail)-1)
    avatar = str(ctx.author.avatar.url)

    resp = f'''Hi {ctx.author.mention},
Your idea for art this time is ||**{art_ideas[idx]} **||'''  # .format(idea=art_ideas[idx])
    file = discord.File(f'{thumbnails}{thumbnail[idx2]}')

    embed = discord.Embed(
        title="Art Idea", description=resp, color=0x0099FF)
    embed.set_thumbnail(url=f'attachment://{thumbnail[idx2]}')
    embed.set_footer(text= f'/help for all availalbe commands', icon_url= avatar )

    await ctx.respond(embed=embed, file=file)

@bot.slash_command(guild_ids=config.guilds, description="Sketch Idea Image")
async def sketch_idea(ctx):
    await ctx.response.defer()
    sketch = [f for f in os.listdir(config.sketch_ideas)]
    number=len(sketch)

    idx = random.randint(0, number-1)
    avatar = str(ctx.author.avatar.url)
    file = discord.File(f'{sketch_ideas}{sketch[idx]}')

    resp = f'''Hi {ctx.author.mention},
Here's a picture for you to try to sketch'''  # .format(idea=art_ideas[idx])

    embed = discord.Embed(
        title="Sketch Idea", description=resp, color=0x0099FF)
    embed.set_image(url=f'attachment://{sketch[idx]}')
    embed.set_footer(text= f'/help for all availalbe commands. {number-1} images left', icon_url= avatar )

    await ctx.respond(embed=embed, file=file)
    print(f'{sketch_ideas}{sketch[idx]}')
    os.remove(f'{sketch_ideas}{sketch[idx]}')


@bot.slash_command(guild_ids=config.guilds, description="Command List")
async def help(ctx):
    await ctx.response.defer()
    idx = random.randint(0, len(thumbnail)-1)
    avatar = str(ctx.author.avatar.url)

    file = discord.File(f'{thumbnails}{thumbnail[idx]}')

    resp = '''Available commands:
**/help:** View all available commands
**/idea:** Get idea for art sketch
**/sketch_idea:** Get an image to sketch'''
    embed = discord.Embed(
        title="Help (Command List)", description=resp, color=0x0099FF)
    embed.set_thumbnail(url=f'attachment://{thumbnail[idx]}')
    embed.set_footer(text= f'/help for all availalbe commands', icon_url= avatar )

    await ctx.respond(file=file, embed=embed, ephemeral=True)

bot.run = bot.run(config.bot_token)
