"""
This module logs every use of the Howling Abyss Discord Bot's primary command "gen" / "generate" with the client's
Discord username and ID.

Author: Ryan Tran
Date Last Modified: 5/17/2021
"""


def log(author):
    with open("users.txt", "a+") as usersFile:
        usersFile.write(f"{author}\n")
