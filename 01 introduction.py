#!/usr/bin/env python3
 
###########################################################
#      __                     _____                       #
#   __|  |___ ___ ___ ___ ___|  |  |                      #
#  |  |  | -_|_ -| . | -_|  _|  |  |                      #
#  |_____|___|___|  _|___|_|  \___/                       #
#                |_|                                      #
# encoding: utf                                           #
# Copyright (c) 2020 Jesper Vang <jesper_vang@me.com>     #
# MIT Licence. See http://opensource.org/licenses/MIT     #
# Created on 4 Jul 2020                                       #
###########################################################

"""
This is code for the introduction chapter. As such, it stands alone
and won't be used anywhere else in the book.
"""
# type: ignore

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}

# And loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
    friendships[i].append(j)  # Add j as a friend of user i
    friendships[j].append(i)  # Add i as a friend of user j