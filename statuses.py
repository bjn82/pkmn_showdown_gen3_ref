#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:18:47 2019

@author: brennandonnell
"""
#%%  IMPORTS

import pickle

#%%
"""
Basic setup about this:
{
Status: status name,
ABBR: abbreviation,
Type: volatile, nonvolatile, volatile battle status
Description:, text
}
"""

burn = {
        'Status': 'Burn',
        'Abbreviation': 'BRN',
        'Type': 'Non-volatile',
        'Description': 'Deals damage equal to 1/8 of max HP at the end of each turn. Also halves the Attack stat. Fire pokemon cannot be burnt.'
        }

freeze = {
        'Status': 'Freeze',
        'Abbreviation': 'FRZ',
        'Type': 'Non-volatile',
        'Description': 'The pokemon is stuck in ice and cannot move until thawed. There is a 20% chance to thaw out each time it tries to move. Once thawed, the pokemon can attack immediately. Any damaging fire move can thaw a frozen target with the exception of Hidden Power Fire. Freezing also disables the ability Flash Fire. Ice-type pokemon cannot be Frozen, nor can pokemon with the Magma Armor ability.'
        }

paralysis = {
     'Status': 'Paralysis',
     'Abbreviation': 'PAR',
     'Type': 'Non-volatile',
     'Description': 'The pokemon has a 25% risk of being immobilized and not moving during the turn. Additionally, it has its speed is reduced by 75%.'
     }

poison = {
     'Status': 'Poison',
     'Abbreviation': 'PSN',
     'Type': 'Non-volatile',
     'Description': 'The pokemon takes damage equal to 1/8 of its max HP each turn.'
     }

toxic = {
     'Status': 'Toxic',
     'Abbreviation': 'TOX',
     'Type': 'Non-volatile',
     'Description': 'The pokemon is badly poisoned. Initially it takes damage equal to 1/16 of its max HP, but that increases by 1/16 each turn. The counter resets when the pokemon is switched out.'
     }

sleep = {
     'Status': 'Sleep',
     'Abbreviation': 'SLP',
     'Type': 'Non-Volatile',
     'Description': 'This pokemon is asleep. IT cannot attack or use moves, with the exception of Snore and Sleep Talk. It lasts for a predetermined number of turns in the range of 1 to 5 turns. Using Rest puts the user asleep for 2 turns.'
     }

#%%

non_vol = [burn, freeze, paralysis, poison, toxic, sleep]

#%%
def make_pickles(ls = non_vol): #this may change later
    for itm in ls:
        with open('statuses/' + itm['Status'] + '.pickle', 'wb') as output_file:
            pickle.dump(itm, output_file)
        
#%%
print('List of Abilities, sorted alphabetically:')
letter = 'B'
print('B')
for ind,val in enumerate(non_vol):
    if val['Status'][0] != letter:
        letter = val['Status'][0]
        print(letter)
    print('\t',ind, val['Status'])
#%%

#d = {
#     'Status': '',
#     'Abbreviation': '',
#     'Type': '',
#     'Description': ''
#     }