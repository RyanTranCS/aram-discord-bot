"""
This program was created to simulate the champion reroll system in the normal ARAM game mode of League of Legends,
for use in the custom ARAM game mode, where the champion reroll system is not implemented.

In the ARAM game mode, each player on both teams is given a random champion from the pool of available champions.
Players have the option of "rerolling" their champion if they do not wish to play their originally selected champion.

The bot accepts 2 integers as arguments to its primary command, "generate." The 1st is the amount of players on
each team, and the 2nd is the amount of rerolls each player is given.

Author: Ryan Tran
Date Last Modified: 5/17/2021
"""

import discord

import logger
import team_generator
from discord.ext import commands

bot = commands.Bot(command_prefix='.')


# once bot is online and ready
@bot.event
async def on_ready():
    print("ARAM Generator Bot Online: Hello, World!")

    numServers = len(bot.guilds)
    print(f"Connected on {numServers} Servers")


# primary command, "generate"
@bot.command(name='generate', aliases=['gen'])
async def generate(ctx, players_per_team: int, rerolls_per_player: int):
    # log author of command caller
    logger.log(ctx.message.author)

    champions_per_team = players_per_team + players_per_team * rerolls_per_player

    # create embedded message to be sent on server
    embed = discord.Embed(title='ARAM Teams Generator', color=0x64AADE)
    embed.add_field(name='Players Per Team', value=players_per_team, inline=True)
    embed.add_field(name='Rerolls Per Player', value=rerolls_per_player, inline=True)
    embed.add_field(name='Champions Per Team', value=champions_per_team, inline=True)

    # generate teams based on author's input
    # returns tuple containing teams if successful; returns error message otherwise
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


bot.run("")
