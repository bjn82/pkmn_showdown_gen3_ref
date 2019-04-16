#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:33:49 2019

@author: brennandonnell

The purpose of this code is to do monotype weaknesses
"""

#%%
"""
Imports
"""
import argparse
import pickle

#%% 
"""
basic outline of the structure for move types

{
Type: [],
2x effective: [],
1/2 effective: [],
Nullified by: []
}
"""
TYPE_CODES = ['bug', 'dark', 'dragon', 'electric', 'fighting',
             'fire', 'flying', 'ghost', 'grass', 'ground', 'ice',
             'normal', 'poison', 'psychic', 'rock', 'steel', 'water']
#%%

"""
Basic outline of the pokemon types
{
type:[],
4x weak: [],
2x weak: [],
1/2 damage: [],
1/4 damage: [],
immunities: []
}
If a type appears twice in a list, it goes to either 4x from 2x or 1/4 from 1/2
if a type appears for weakness or resistance and in immunities, immunities has 
priority
"""

def load_data(value):
    """
    Loads a type, input is a string from command line. 
    """
    t_1 = None
    if value != None:
        with open("types/" + value + ".pickle", "rb") as input_file:
            t_1 = pickle.load(input_file)
    return(t_1)
    

def is_valid_type(value):
    """
    Checks to see if input value is a valid type for gen 3
    """
    value = value.lower()
    if value not in TYPE_CODES:
        raise argparse.ArgumentTypeError("%s is an invalid type" % value)
    return value

        
def monotype(d):
    """
    Query a type, and get its resistances and weanesses returned. 
    """
    return d

#%%
# main stuff

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('type1', type=is_valid_type)
    args = parser.parse_args()

    type1 = load_data(args.type1)
    
    found = monotype(type1)
    
    print('Type:', found['Type'])
    print('4x weak:', found['4x weak'])
    print('2x weak:', found['2x weak'])
    print('1/2 dmg:', found['1/2 dmg'])
    print('1/4 dmg:', found['1/4 dmg'])
    print('immunities:', found['immunities'])
    
