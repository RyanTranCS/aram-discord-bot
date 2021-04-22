"""
This program was created to simulate the champion reroll system in the normal ARAM game mode of League of Legends,
for use in the custom ARAM game mode, where the champion reroll system is not implemented.

In the ARAM game mode, each player on both teams is given a random champion from the pool of available champions.
Players have the option of "rerolling" their champion if they do not wish to play their originally selected champion.

The bot accepts 2 integers as arguments to its primary command, "generate." The 1st is the amount of players on
each team, and the 2nd is the amount of rerolls each player is given.

Author: Ryan Tran
Date Last Modified: 3/9/2021
"""

import discord
import logging
import team_generator
from discord.ext import commands

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix='.')


# once bot is online and ready
@bot.event
async def on_ready():
    print("ARAM Generator Bot Online: Hello, World!")


# primary command, "generate"
@bot.command(name='generate', aliases=['gen'])
async def generate(ctx, players_per_team: int, rerolls_per_player: int):
    champions_per_team = players_per_team + players_per_team * rerolls_per_player

    embed = discord.Embed(title='ARAM Generator', color=0x879BC0)
    embed.add_field(name='Players Per Team', value=players_per_team, inline=True)
    embed.add_field(name='Rerolls Per Player', value=rerolls_per_player, inline=True)
    embed.add_field(name='Champions Per Team', value=champions_per_team, inline=True)

    teams = team_generator.generate_teams(players_per_team, rerolls_per_player)

    if type(teams) is tuple:
        str_team_1 = team_generator.format_team(teams[0])
        str_team_2 = team_generator.format_team(teams[1])
        embed.add_field(name='Team 1 (Blue Team)', value=str_team_1, inline=True)
        embed.add_field(name='Team 2 (Red Team)', value=str_team_2, inline=True)
    else:
        embed.add_field(name='Error', value=teams, inline=True)

    await ctx.send(embed=embed)


# if an error occurs
@generate.error
async def generate_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        arg_error_message = "Please enter 2 integers separated by a space! (e.g. \".gen 5 2\")"

        embed = discord.Embed(title='Generation Error', color=0x879BC0)
        embed.add_field(name='Invalid Input', value=arg_error_message, inline=True)

        await ctx.send(embed=embed)


bot.run("ODAxMjEwNDU2MDU2Mzk3ODc0.YAdXYg.tg3qDQFzUJVtRAWqLt0kuHsCLFo")
