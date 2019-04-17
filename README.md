# pkmn_showdown_gen3_ref
A python3 command line reference tool to help look up resistances and weaknesses, as well as what each ability does. 

My friends and I have been playing [Pokemon Showdown](https://pokemonshowdown.com/) for a few months and we're hooked. Some of us have different experiences with different generations. 

Despite this, we decided to do a Gen III tournament. In order to improve my type-knowledge and general skill, I started researching the different types. Type charts are helpful for monotype pokemon, but with dual-types it can be a bit harder to keep track of on the fly, especially with abilities thrown in. Thus, I decided to write this program.

Sure, something like this may already exist, but I didn't think of that when I set out to make it. I wanted it to be helpful for my friends and for myself. To help level the playing field for those who aren't used to Gen 3. 

I'm not affiliated with Pokemon Showdown, Nintendo, Creatures Inc, etc. I just like doing random battles and writng python code. 

---

### How to use: 

navigate to the folder in the command line. 
* To view the attributes, strengths, and weaknesses of monotype pokemon, run ```python monotype.py type``` where *type* is the type to view. 
* To view the attributes, strengths, and weaknesses of dualtype pokemon, run ```python dualtype.py type1 type2``` where *type1* is the primary type and *type2* is the secondary type.  
* To look up what an ability does, run ```python ability.py ability``` where *ability* is the ability in question. If the ability is two words, like Pure Power or Air Lock, enclose the ability in quotes. For example, if I wanted to find out what Air Lock did, I would run ```python ability.py 'air lock'```. 
* To view the list of types sorted alphabetically, run ```python types.py```.
* To view the list of abilities sorted alphabetically, run ```python abilities.py```.

The **types** are dictionaries stored as pickles in the *types* folder. Likewise, the **abilities** are stored in the *abilities* folder are in the format of pickled dictionaries. 

If for some reason, a type or ability is missing, try re-running either `abilities.py` or `types.py`. Those have the code to create the dictionaries and pickle them. If you would like to expand this code to work for future generations, those two pieces of code are the ones to modify. 

Requirements: 
* Python 3
  + pickle
  + argparser


---

## Progress Report: 

**04/17/19:**
* Abilities are completed. 
* Merged branches with the tested (but still incomplete) `ability.py` and `abilities.py`. 

**04/16/19:** 
* Initial commit
* `dualtype.py`, `monotype.py` are completed and have been tested in Terminal on Mac OS and Windows 
* `ability.py` and `abilities.py` are nearly completed. I'm on the *S* abilities. The `ability.py` program does run from terminal on Mac OS and Windows. 

## Future ideas: 
* Add a search function to `abilities.py` (and possibly `types.py`, though that may not be as useful). 
* Modify `abilities.py` and `types.py` so that each time those are executed, they don't remake each of the pickles. 
* Maybe someday down the road implement a status affliction reference. 
