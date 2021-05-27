"""
This program was created to simulate the champion reroll system in the normal ARAM game mode of League of Legends,
for use in the custom ARAM game mode, where the champion reroll system is not implemented.

In the ARAM game mode, each player on both teams is given a random champion from the pool of available champions.
Players have the option of "rerolling" their champion if they do not wish to play their originally selected champion.

The bot accepts 2 integers as arguments to its primary command, "generate." The 1st is the amount of players on
each team, and the 2nd is the amount of rerolls each player is given.

Author: Ryan Tran
Date Last Modified: 5/27/2021
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
    embed = discord.Embed(title='ARAM Teams', color=0x64AADE)
    embed.add_field(name='Players Per Team', value=players_per_team, inline=True)
    embed.add_field(name='Rerolls Per Player', value=rerolls_per_player, inline=True)
    embed.add_field(name='Champions Per Team', value=champions_per_team, inline=True)

    num_champions_to_gen = champions_per_team * 2
    num_champions_total = team_generator.get_champions_len()

    # if input is invalid, then generate error message
    if num_champions_to_gen > num_champions_total or num_champions_to_gen <= 0:
        error_message = create_invalid_input_message(num_champions_to_gen, players_per_team, rerolls_per_player)
        embed.add_field(name='Error', value=error_message, inline=True)

    # otherwise, generate teams based on author's input and add them to embedded message
    else:
        teams = team_generator.generate_teams(players_per_team, rerolls_per_player)

        str_team_1 = team_generator.format_team(teams[0])
        str_team_2 = team_generator.format_team(teams[1])
        embed.add_field(name='Team 1 (Blue Team)', value=str_team_1, inline=True)
        embed.add_field(name='Team 2 (Red Team)', value=str_team_2, inline=True)

    await ctx.send(embed=embed)


def create_invalid_input_message(num_champions_to_gen, players_per_team, rerolls):
    num_champions = team_generator.get_champions_len()

    if num_champions_to_gen > num_champions:
        error_message = f"Invalid Input: The total number of champions requested to be generated" \
                        f" must not exceed the total number of champions in the game ({num_champions}).\n\n" \
                        f"Requested Number of Champions: \nPlayers Per Team ({players_per_team}) x " \
                        f"Rerolls Per Player ({rerolls}) x Teams (2) = {num_champions_to_gen}"
    elif num_champions_to_gen <= 0:
        error_message = f"Invalid Input: The total numbers of champions requested to be generated is 0 or less."

    return error_message


# if an error occurs
@generate.error
async def generate_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        arg_error_message = "Please enter 2 integers separated by a space! (e.g. \".gen 5 2\")"

        embed = discord.Embed(title='Generation Error', color=0x879BC0)
        embed.add_field(name='Invalid Input', value=arg_error_message, inline=True)

        await ctx.send(embed=embed)


bot.run("")
