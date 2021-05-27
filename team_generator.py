"""
This module implements the generation of teams, which consists of appending randomly chosen champions from a list
containing all of the champions in the game to lists representing teams. It is also able to format the lists
it produces.

It accepts as input the amount of players per team and the amount of rolls each player on each team is given,
which are arguments to the primary command "generate" in main.

Author: Ryan Tran
Date Last Modified: 5/27/2021
"""

import random

CHAMPIONS = []

# appends string champion names to list
with open('C:/Users/Ryan/PycharmProjects/HowlingAbyssDiscordBot/LoLChampions.txt') as f:
    CHAMPIONS = f.read().splitlines()

CHAMPIONS_LENGTH = len(CHAMPIONS)


def generate_teams(players_per_team, rerolls):
    """
    This method calculates the amount of champions to be generated per team using the given input and supplies 2 calls
    to the generate_team method with the processed info.

    :param players_per_team: the amount of players per team
    :param rerolls: the amount of rerolls each player should have
    :return: valid input -> tuple of 2 lists (the teams)
    """

    champions_per_team = players_per_team + (players_per_team * rerolls)

    # creates a copy of the global array for local use
    # IMPORTANT: not creating a copy would have future function calls access a previously modified global array
    local_champions = CHAMPIONS[:]

    team_1 = generate_team(local_champions, champions_per_team)
    team_2 = generate_team(local_champions, champions_per_team)

    return team_1, team_2


def generate_team(available_champions, champions_per_team):
    """
    This method generates a team of random champions.

    :param available_champions: a list of champions to randomly choose from, shared with another call of generate_team
    :param champions_per_team: the amount of champions to be generated per team
    :return: list containing strings of champion names
    """

    rand_max = len(available_champions) - 1     # upper bound of random number generator
    team = []                                   # list to be returned

    for i in range(champions_per_team):
        random_champion_ID = random.randint(0, rand_max)                # inclusive range -> [0, rand_max]
        random_champion = available_champions.pop(random_champion_ID)   # pops champion from list, "marking" it as used
        team.append(random_champion)                                    # adds champion to team

        rand_max = rand_max - 1  # decrements max, as a champion was popped

    return team


def format_team(team):
    """
    This method converts a team contained within a list into a neatly formatted string.

    :param team: list of strings of champion names
    :return: none
    """

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
