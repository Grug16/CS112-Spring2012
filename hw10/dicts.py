#!/usr/bin/env python
"""
THIS IS THE PRE-MIDNIGHT VERSION.  ADVANCED LATER TONIGHT

dicts.py

Dictionaries
============================================================ 
In this section, write some functions which build and 
manipulate python dictionaries.
"""

# 1. freq
#      Return a dictionary of the number of times each value
#      is in data.
#          >>> freq([ 1, 2, 2, 2, 2, 3, 4, 5, 1, 4, 1, 9, 10 ])
#          { 1: 3, 2: 4, 3: 1, 4: 1, 5: 1, 9: 1, 10: 1}

def freq(data):
    "calculate the frequency for each value in data"



# 2. Movie Reviews
#      Write two functions to help with scoring a movie.
#
#      score:
#        stores a score in the "movies" dictionary
#
#      avg_score:
#        returns the average score of a movie
#
#      Examples:
#      >>> score("Fargo", 4)
#      >>> score("Fargo", 5)
#      >>> score("Fargo", 5)
#      >>> avg_score("Fargo")
#      4.6666666667
#      >>> avg_score("missing movie")
#      None

"""
if not title in movies:
movies[title] = []
if value = None
    return
movies[title].append(value)

def avg score (title)
total = 0
for v in movies(title):
total += v
return total / len(movie[title])


"""
movies = {}

def score(title, value):
    "register the score for a given movie out of 5"
    if not title in movies:
        movies[title] = []
    if value == None:
        return
    movies[title].append(value)


def avg_score(title):
    if title not in movies:
        return None
    "return the average score for a given movie"
    total = 0.0
    for v in movies[title]:
        total += v
    return total / len(movies[title])



# 3. parse_csv (Advanced)
#        Takes an input string and spits back a list of comma
#        separated values (csv) entries.  Hint, check the zip
#        and dict functions.
#
#        The point of this is to create your own parser, not to
#        use pythons builtin 'csv' library.
#
#           >>> csv = """
#           name,age,email
#           Foo, 24, foo@example.com
#           Bar ,22 ,bar@example.com
#           Baz, 20 , baz@gmail.com
#           """
#           >>> parse_csv(csv)
#           [ { "name": "Foo", "age": "24", "email": "foo@example.com" },
#             { "name": "Bar", "age": "22", "email": "bar@example.com" },
#             { "name": "Baz", "age": "20", "email": "baz@example.com" } ]            
#
# dict(zip(('one', 'two'), (1, 2)))
# {"one": 1, "two": 2}
"""
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> zipped
[(1, 4), (2, 5), (3, 6)]
"""


# raw_input(msg).strip()
 #   return [ int(c.strip()) for c in inp.split(",") ]
 # splits everything at  the Comma, then strips the excess.

def parse_csv(data):
    "parses a csv file into a list of dictionaries"
    newlist = data.splitlines()
    stripped_list = [line.strip() for line in newlist]
    zip(newlist)
    dict(newlist)

    




