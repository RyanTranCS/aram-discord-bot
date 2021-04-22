"""
This module implements the generation of teams, which consists of appending randomly chosen champions from a list
containing all of the champions in the game to lists representing teams. It is also able to format the lists
it produces.

It accepts as input the amount of players per team and the amount of rolls each player on each team is given,
which are arguments to the primary command "generate" in main.

Author: Ryan Tran
Date Last Modified: 3/9/2021
"""

import random

CHAMPIONS = []

with open('C:/Users/Ryan/PycharmProjects/HowlingAbyssDiscordBot/LoLChampions.txt') as f:
    CHAMPIONS = f.read().splitlines()

CHAMPIONS_LENGTH = len(CHAMPIONS)


def generate_teams(players_per_team, rerolls):
    champions_per_team = players_per_team + (players_per_team * rerolls)
    total_champions = champions_per_team * 2

    if total_champions > CHAMPIONS_LENGTH:
        error_message = f"Invalid Input: The total number of champions requested to be generated" \
                        f" must not exceed the total number of champions in the game ({CHAMPIONS_LENGTH}).\n\n" \
                        f"Requested Number of Champions: \nPlayers Per Team ({players_per_team}) x Teams (2) x " \
                        f"Rerolls Per Player ({rerolls}) = {total_champions}"
        return error_message

    elif total_champions <= 0:
        error_message = f"Invalid Input: The total amount of champions requested to be generated is 0 or less."
        return error_message

    else:
        # creates a copy of the global array for local use
        # IMPORTANT: not creating a copy would have future function calls access a previously modified global array
        local_champions = CHAMPIONS[:]

        team_1 = generate_team(local_champions, champions_per_team)
        team_2 = generate_team(local_champions, champions_per_team)

        return team_1, team_2


def generate_team(available_champions, champions_per_team):
    rand_max = len(available_champions) - 1
    team = []

    for i in range(champions_per_team):
        random_champion_ID = random.randint(0, rand_max)                # inclusive range -> [0, rand_max]
        random_champion = available_champions.pop(random_champion_ID)   # pops champion from list, "marking" it as used
        team.append(random_champion)                                    # adds champion to team

        rand_max = rand_max - 1  # decrements max, as a champion was popped

    return team


def format_team(team):
    number_of_champions = len(team)
    str_team = ''

    for i in range(number_of_champions - 1):
        str_team = str_team + f"{i + 1}. {team[i]}\n"

    str_team = str_team + f"{number_of_champions}. {team[number_of_champions - 1]}"

    return str_team


def get_champions_len():
    return CHAMPIONS_LENGTH


def get_champion_at(index):
    return CHAMPIONS[index]
