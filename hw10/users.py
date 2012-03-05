#!/usr/bin/env python
"""
>>> CALLING IT QUITS AT 4AM.  FOAF IS GIVING ME CONTRADICTORY ERRORS, IE "NOT A
SET" WHEN IT IS CLEARLY A SET


users.py 

User Database (Advanced)
=========================================================
The nice thing about dictionaries (and objects) is you can 
have a list or a dictionary of items that all have the same 
properties.  The result is something like a lookup table or 
a database

For the following examples, assume that users is a list that
looks something like this:
    users = {
       "Ben S": { "age": 23, "follows": [ "Sally F", "Gerald Q" ] },
       "Sally F": { "age": 10, "follows": [ "Gerald Q", "Frank L" ] },
       "Jeff B":  { "age": 12, "follows": [ "Steve M", "Sally F", "Gerald Q" ] },
       "Gerald Q": { "age": 20, "follows": [ ] },
       "Steve M": { "age": 18, "follows": [ ] },
       ...
     }

You can see the actual data as a table in users_data.txt
"""

import sets
#  USERS['Lola']['follows']
# 1. followers
#      Find everyone who is following the given names.  Using the 
#      above example:
#          >>> followers(users, "Gerald Q", "Sally F")
#          [ "Ben S", "Sally F", "Jeff B", "Steve M" ]
#
#       Hint, lookup "set" in python

def followers(users, *names):
    "find followers for given names"
    from sets import Set
    data = Set([])
    for target in names:
        for name in users:
            if target in users[name]['follows']:
                data.add(name)
    #    data.add(Set(users[x]['follows']))
    print "Followers:  \n",data
    return data


# 2. underage_follows
#      Find everyone that underage users (age <= 12) follow.  Make
#      sure there are no duplicates.  Do not include the underage
#      users themselves
#          >>> underage_follows(users)
#          [ "Steve M", "Gerald Q", "Frank L" ]

def underage_follows(users):
    "find who underage users follow"
    from sets import Set
    data = Set([])
    children = []
    for x in users:
        if users[x]['age'] <= 12:
            children.append(x)
            data = data | (Set(users[x]['follows']))
    for name in children:
        if data.__contains__(name):
            data.remove(name)
    return data



# 3. foaf 
#      Foaf (friend of a freind) returns a list of everyone whom 
#      a user's followers follow not including the user themself.
#         >>> foaf(users, "Gerald Q")
#         [ "Sally F", "Frank L", "Steve M" ]

def foaf(users, name):
    "find everyone whom a user's followers follow (not including user)"
    from sets import Set
    data = Set([])
    usednames = []
    for x in followers(users, name):
        usednames.append(x)
        data = data | (Set(users[x]['follows']))
    for aname in usednames:
        if data.__contains__(aname):
            data.remove(aname)
    data.remove(name)
    print "foaf: \n",data
    return data

"""

def followers(users, *names):
    "find followers for given names"
    from sets import Set
    data = Set([])
    for target in names:
        for name in users:
            if target in users[name]['follows']:
                data.add(name)
    #    data.add(Set(users[x]['follows']))
    return data
"""



# 4. age_demographics
#       For "statistics", return a dictionary with the average age 
#       of the followers for a given user age.  So, for example, 
#       find the average age of EVERYONE who follows someone who is 
#       19.
#
#       Sample output:
#         { 19: 20.33333333,
#           20: 24.125,
#           21: 17 
#           ...
#         }

def age_demographics(users):
     "calculate age demographics"



# UNCOMMENT THE FOLLOWING TO WRITE YOUR OWN CODE USING USERS
# if __name__ == "__main__":
#    from tests.test_users import USERS
#    print USERS

