#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:34:33 2019

The purpose of this code is to create the types in pickles. 
Run if there are types missing. 

@author: brennandonnell
"""

#%%
"""
Imports
"""

import pickle

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

fire = {
        'Type': ['fire'],
        '4x weak':[],
        '2x weak':['water','ground','rock'],
        '1/2 dmg':['fire','grass','ice','bug','steel'],
        '1/4 dmg':[],
        'immunities':[]
        }

flying = {
        'Type': ['flying'],
        '4x weak':[],
        '2x weak':['rock','electric','ice'],
        '1/2 dmg':['grass','fighting','bug',],
        '1/4 dmg':[],
        'immunities':['ground']
        }

water = {
        'Type': ['water'],
        '4x weak':[],
        '2x weak':['grass','electric'],
        '1/2 dmg':['water','steel','fire','ice'],
        '1/4 dmg':[],
        'immunities':[]
        }

grass = {
        'Type': ['grass'],
        '4x weak':[],
        '2x weak':['fire','ice','poison','flying','bug'],
        '1/2 dmg':['water','electric','grass','ground'],
        '1/4 dmg':[],
        'immunities':[]
        }

normal = {
        'Type': ['normal'],
        '4x weak':[],
        '2x weak':['fighting'],
        '1/2 dmg':[],
        '1/4 dmg':[],
        'immunities':['ghost']
        }

fighting = {
        'Type': ['fighting'],
        '4x weak':[],
        '2x weak':['flying', 'psychic'],
        '1/2 dmg':['dark','rock','bug'],
        '1/4 dmg':[],
        'immunities':[]
        }

dark = {
        'Type': ['dark'],
        '4x weak':[],
        '2x weak':['fighting','bug'],
        '1/2 dmg':['ghost','dark'],
        '1/4 dmg':[],
        'immunities':['psychic']
        }

poison = {
        'Type': ['poison'],
        '4x weak':[],
        '2x weak':['psychic','ground'],
        '1/2 dmg':['fighting','poison','bug','grass'],
        '1/4 dmg':[],
        'immunities':[]
        }

ground = {
        'Type': ['ground'],
        '4x weak':[],
        '2x weak':['grass','ice','water'],
        '1/2 dmg':['poison','rock'],
        '1/4 dmg':[],
        'immunities':['electric']
        }

steel = { 
        'Type': ['steel'],
        '4x weak':[],
        '2x weak':['fighting','fire', 'ground'],
        '1/2 dmg':['normal','flying','psychic',
                   'rock','steel','dragon',
                   'grass','bug','ice'],
        '1/4 dmg':[],
        'immunities':['poison']
        }

ghost = { 
        'Type': ['ghost'],
        '4x weak':[],
        '2x weak':['ghost','dark'],
        '1/2 dmg':['poison','bug'],
        '1/4 dmg':[],
        'immunities':['normal','fighting']
        }

dragon = { 
        'Type': ['dragon'],
        '4x weak':[],
        '2x weak':['dragon','ice'],
        '1/2 dmg':['fire','water','electric','grass'],
        '1/4 dmg':[],
        'immunities':[]
        }

psychic = { 
        'Type': ['psychic'],
        '4x weak':[],
        '2x weak':['dark','bug','ghost'],
        '1/2 dmg':['fighting','psychic'],
        '1/4 dmg':[],
        'immunities':[]
        }

electric = { 
        'Type': ['electric'],
        '4x weak':[],
        '2x weak':['ground'],
        '1/2 dmg':['flying','steel','electric'],
        '1/4 dmg':[],
        'immunities':[]
        }

rock = { 
        'Type': ['rock'],
        '4x weak':[],
        '2x weak':['fighting','steel', 'ground','water','grass'],
        '1/2 dmg':['normal','flying','poison','fire'],
        '1/4 dmg':[],
        'immunities':[]
        }

bug = { 
        'Type': ['bug'],
        '4x weak':[],
        '2x weak':['fire','flying','rock'],
        '1/2 dmg':['ground','fighting','grass'],
        '1/4 dmg':[],
        'immunities':[]
        }

ice = { 
        'Type': ['ice'],
        '4x weak':[],
        '2x weak':['fighting','fire', 'rock', 'steel'],
        '1/2 dmg':['ice'],
        '1/4 dmg':[],
        'immunities':[]
        }

type_list = [bug, dark, dragon, electric, fighting,
             fire, flying, ghost, grass, ground, ice,
             normal, poison, psychic, rock, steel, water]

for itm in type_list:
    with open('types/' + itm['Type'][0] + '.pickle', 'wb') as output_file:
        pickle.dump(itm, output_file)
        
        
#%%
print('List of Types, sorted alphabetically:')
letter = 'B'
print('B')
for ind,val in enumerate(type_list):
    if val['Type'][0][0].upper() != letter:
        letter = val['Type'][0][0].upper()
        print(letter)
    print('\t',ind, val['Type'][0])