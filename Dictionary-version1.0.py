# this program will be an interactive English dictionary where the user inputs
# a word and the program will return all available definitions associated
# with that word.  The code should also be smart enough to recognize user input
# error and correct it.  Example: user inputs 'rainn' and program responds with:
# "did you mean rain? Y/N"

# Author: Tyler Elenberger
# date started: 6/23/20
# date ended: 7/3/20
# version 1 of code,
# version 2 to include user interface and mysql database

import json
from difflib import get_close_matches
from tkinter import *                               # turning this into user interface
import mysql.connector                              # for when data will be transferred from json to mysql database

# loading the data from mysql will be quicker than using the given json file

data = json.load(open("data.json"))                 # data.json contains ALL words associated w/ definitions in form of dict

def definition(word):
    word = word.lower()                             # account for case sensitivity
    if word in data:
        return data[word]
    elif word.title() in data:                      # accounts for dict keys that are capitalized
        return data[word.title()]
    elif word.upper() in data:                      # accounts for acronyms (USA, NATO, etc.)
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.75)) > 0:    # get_close_matches returns list, check to see if item is in list
        answer = input("Did you mean %s? (Y for yes/N for no): " % get_close_matches(word, data.keys())[0])   # ask for first item of list (if multiple items)
        if answer == 'Y' or answer == 'yes' or answer == 'Yes' or answer == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif answer == 'N' or answer == 'no' or answer == 'No' or answer == 'n':         # giving user as many chances to get it right
            try:
                user = input("Enter your word here: ")
            except:
                return "Invalid input!"
            else:
                return data[user] if user in data else definition(word)
        else:
            return "Invalid input!"
    else:
        return "Could not find word in dictionary"

user = input("Enter your word here: ")
output = definition(user)

if type(output) == list:        # a way to format multiple defs in a neater fashion
    for d in output:
        print("-",d)
else:
    print(output)               # for one def words 
