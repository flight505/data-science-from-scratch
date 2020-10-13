#!/usr/bin/env python3
 
##########################################################
# encoding: utf                                          #
# Copyright (c) Jesper Vang <jesper_vang@me.com>         #
# MIT Licence. See http://opensource.org/licenses/MIT    #
# Created on 5 Jul 2020                                  #
##########################################################


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

# list of pairs 
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

#  for each user id:
friendships = {user["id"]: [] for user in users}
#print(friendships)

# And loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
    friendships[i].append(j)  # Add j as a friend of user i
    friendships[j].append(i)  # Add i as a friend of user j

def number_offriends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"]
    print(user_id)
    friend_ids = friendships[user_id]
