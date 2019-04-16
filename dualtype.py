#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:14:18 2019

@author: brennandonnell

The purpose of this is to look at dual-type pokemon strenghts & weaknesses
for gen 3. 
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
    
#def is_valid_type2(value):
#    """
#    Checks to see if input value is a valid type for gen 3
#    Wrapper for second type if looking into dualtype
#    """
#    if value != None:
#        return is_valid_type(value)
#    else: # meaning monotype
#        return None
    
    
def listcheck(ls, dup = []):
    """
    Search a list for multiple occurences,
    if they are found, remove those occurences and put them into a new list
    
    @param: ls list
    @param: dup: duplicate list
    """
    
    for s in ls:
        if ls.count(s) > 1:
            dup.append(s)
            while(ls.count(s) > 0):
                ls.remove(s)
    return ls, dup

def immunize(ls, im):
    """
    checks whether a weakness is also nullified
    
    @param ls: lsit
    @param im, immunity list
    """
    for s in im:
        if s in ls:
            ls.remove(s)
            im.append(s)
            
        if im.count(s) > 1:
            while im.count(s) > 1:
                im.remove(s)
    return ls, im

def normalize(res, weak):
    """
    looks for if things are resistant and weak
    removes things that are both weak and strong
    e.g.: fire flying isn't weak to ice
    
    @param: res: list
    @param: weak: list
    """
    rem = []
    for r in res:
#        print(r)
        if r in weak:
            rem.append(r)
    for r in rem:   
        res.remove(r)
        weak.remove(r)

    return res, weak
        
def monotype(d):
    """
    Query a type, and get its resistances and weanesses returned. 
    """
    return d
    


def dualtype(d1, d2):
    """
    puts together two types into d1
    """
    if d2 == None:
        return monotype(d1)
    else:
        z = {
            'Type': [],
            '4x weak':[],
            '2x weak':[],
            '1/2 dmg':[],
            '1/4 dmg':[],
            'immunities':[]
            }
        for key in z.keys():
            f = list(d1[key])
            g = list(d2[key])
            f.extend(g)
            z[key].extend(f)
            
    #    print(z)
            
        z['2x weak'], z['4x weak'] = listcheck(z['2x weak'], dup=z['4x weak'])
        z['1/2 dmg'], z['1/4 dmg'] = listcheck(z['1/2 dmg'], dup=z['1/4 dmg'])
        
        z['1/2 dmg'], z['2x weak'] = normalize(z['1/2 dmg'], z['2x weak'])
        z['2x weak'], z['1/2 dmg'] = normalize(z['2x weak'], z['1/2 dmg'])
    
        z['2x weak'], z['immunities'] = immunize(z['2x weak'], z['immunities'])
        z['1/2 dmg'], z['immunities'] = immunize(z['1/2 dmg'], z['immunities'])
        z['4x weak'], z['immunities'] = immunize(z['4x weak'], z['immunities'])
        z['1/4 dmg'], z['immunities'] = immunize(z['1/4 dmg'], z['immunities'])
    
        return z

#%%
# main stuff

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('type1', type=is_valid_type)
    parser.add_argument('type2', type=is_valid_type)
    args = parser.parse_args()

    type1 = load_data(args.type1)
    type2 = load_data(args.type2)
    
    found = dualtype(type1, type2)
    
    print('Type:', found['Type'])
    print('4x weak:', found['4x weak'])
    print('2x weak:', found['2x weak'])
    print('1/2 dmg:', found['1/2 dmg'])
    print('1/4 dmg:', found['1/4 dmg'])
    print('immunities:', found['immunities'])
    
