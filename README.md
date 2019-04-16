# pkmn_showdown_gen3_ref
A python3 command line reference tool to help look up resistances and weaknesses, as well as what each ability does. 

My friends and I have been playing [Pokemon Showdown](https://pokemonshowdown.com/) for a few months and we're hooked. Some of us have different experiences with different generations. 

Despite this, we decided to do a Gen III tournament. In order to improve my type-knowledge and general skill, I started researching the different types. Type charts are helpful for monotype pokemon, but with dual-types it can be a bit harder to keep track of on the fly, especially with abilities thrown in. Thus, I decided to write this program.

Sure, something like this may already exist, but I didn't think of that when I set out to make it. I wanted it to be helpful for my friends and for myself. To help level the playing field for those who aren't used to Gen 3. 

I'm not affiliated with Pokemon Showdown, Nintendo, Creatures Inc, etc. I just like doing random battles and writng python code. 

---

### How to use: 

navigate to the folder in the command line. 
* To view the attributes, strengths, and weaknesses of monotype pokemon, run ```python3 monotype.py type``` where *type* is the type to view. 
* To view the attributes, strengths, and weaknesses of dualtype pokemon, run ```python3 dualtype.py type1 type2``` where *type1* is the primary type and *type2* is the secondary type.  
* To look up what an ability does, run ```python3 ability.py ability``` where *ability* is the ability in question. 


Requirements: 
* Python 3
  + pickle


---

## Progress Report: 

**04/16/19:** 
* Initial commit
* `dualtype.py`, `monotype.py` are completed and have been tested in Terminal on Mac OS. 
* `ability.py` and `abilities.py` are nearly completed. I'm on the *S* abilities. The `ability.py` program does run from terminal on Mac OS. 
