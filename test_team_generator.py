"""
This unit test checks that the teams generated from team_generator.py contain no duplicate values.
It also checks that boundary values are selected using the random number generation process.

Author: Ryan Tran
Date Last Modified: 3/9/2021
"""

import unittest
import team_generator


class GeneratorTestCase(unittest.TestCase):
    # the following variables are set to values such that maximum coverage is achieved

    champs_len = team_generator.get_champions_len()         # total number of champions in the game
    num_teams = 2                                           # there are always 2 teams
    players_per_team = 1                                    # 1 ensures maximum divisibility in the reroll calculation
    total_players = num_teams * players_per_team            # total amount of players
    base_champs_count = total_players                       # ever player starts with a randomly generated champion
    rerolls_per_player = int(                               # reroll amount such that every champion will be generated
        (champs_len - base_champs_count) / total_players)

    teams = team_generator.generate_teams(players_per_team, rerolls_per_player)
    combined_teams = teams[0] + teams[1]

    def test_for_duplicates(self):
        is_duplicate_present = False

        self.combined_teams.sort()

        for i in range(len(self.combined_teams) - 1):
            if self.combined_teams[i] == self.combined_teams[i + 1]:
                is_duplicate_present = True
                break

        self.assertEqual(is_duplicate_present, False)

    def test_for_boundary_values(self):
        first_champ = team_generator.get_champion_at(0)
        last_champ = team_generator.get_champion_at(self.champs_len - 1)

        are_boundary_values_present = False

        if first_champ in self.combined_teams and last_champ in self.combined_teams:
            are_boundary_values_present = True

        self.assertEqual(are_boundary_values_present, True)


if __name__ == '__main__':
    unittest.main()
