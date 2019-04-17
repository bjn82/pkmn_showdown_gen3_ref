#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:42:25 2019

@author: brennandonnell

Basic setup about this:
{
Status: status name,
ABBR: abbreviation,
Type: volatile, nonvolatile, volatile battle status
Description:, text
}


query a status and get that info about it. 

It is still a work in progress. 
Eventually I would like to have it give info on volatile 
and volatile battle statuses as well. 
"""

#%%
"""
Imports
"""
import pickle
import argparse

#%%
STATUS_CODES = ['burn', 'freeze','paralysis','poison','toxic','sleep'] # will have to fix
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
        with open("statuses/" + value + ".pickle", "rb") as input_file:
            t_1 = pickle.load(input_file)
    return(t_1)
    

def is_valid_status(value):
    """
    Checks to see if input value is a valid ability for gen 3
    """
    value = value.lower()
    
    if value not in STATUS_CODES:
        raise argparse.ArgumentTypeError("%s is an invalid status" % value)
    return value

        
def status(a):
    """
    Query an ability, and get its description returned. 
    """
    return a

#%%
# main stuff

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('status', type=is_valid_status)
    args = parser.parse_args()

    stat = load_data(args.status)
    
    found = status(stat)
    
    print('Status:', found['Status'])
    print('Abbreviation:', found['Abbreviation'])
    print('Type:', found['Type'])
    print('Description:', found['Description'])
    
