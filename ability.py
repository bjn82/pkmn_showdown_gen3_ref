#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:45:58 2019

@author: brennandonnell
"""

#%%
"""
Imports
"""
import pickle
import argparse

#%%
ABILITY_CODES = ['air lock','arena trap', 'battle armor', 'blaze', 'cacophony',
                 'clear body','clorophyll', 'color change', 'compound eyes',
                 'cute charm','damp','drizzle','drought','early bird',
                 'effect spore', 'flame body','flash fire', 'forecast','guts',
                 'huge power','hustle','hyper cutter','illuminate','immunity',
                 'inner focus','insomnia','intimidate','keen eye','levitate',
                 'lightning rod','limber','liquid ooze','magma armor',
                 'magnet pull','marvel scale','minus','natural cure',
                 'oblivious','overgrow', 'own tempo', 'pickup', 'plus', 
                 'poison point', 'pressure', 'pure power', 'rain dish', 
                 'rock head', 'rough skin', 'run away']#,]
#             'fire', 'flying', 'ghost', 'grass', 'ground', 'ice',
#             'normal', 'poison', 'psychic', 'rock', 'steel', 'water']

#%%
"""
This is where you check for abilities. 

The layout of it is in the format of a dictionary

{
Ability: str, # what ability is it
desc: str # how does it work
}

"""
def load_data(value):
    """
    Loads an ability, input is a string from command line. 
    """
    t_1 = None
    if value != None:
        with open("abilities/" + value + ".pickle", "rb") as input_file:
            t_1 = pickle.load(input_file)
    return(t_1)
    

def is_valid_ability(value):
    """
    Checks to see if input value is a valid ability for gen 3
    """
    value = value.lower()
    
    if value not in ABILITY_CODES:
        raise argparse.ArgumentTypeError("%s is an invalid ability" % value)
    return value

        
def ability(a):
    """
    Query an ability, and get its description returned. 
    """
    return a

#%%
# main stuff

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('ability', type=is_valid_ability)
    args = parser.parse_args()

    type1 = load_data(args.ability)
    
    found = ability(type1)
    
    print('Ability:', found['Ability'])
    print('Description:', found['Description'])
    
