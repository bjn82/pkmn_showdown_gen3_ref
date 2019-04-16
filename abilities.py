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

#%%
"""
This is where you check for abilities. 

The layout of it is in the format of a dictionary

{
Ability: str, # what ability is it
desc: str # how does it work
}

"""


air_lock = {
        'Ability': 'Air Lock',
        'Description': 'Negates weather effects.'
        }

arena_trap = {
        'Ability': 'Arena Trap',
        'Description': 'Prevents grounded pokemon from fleeing or switching out.\nSwitching through moves such as baton pass or u-turn are still valid.'
        }

battle_armor = {
        'Ability': 'Battle Armor',
        'Description': 'Blocks critical hits.'
        }

blaze = {
        'Ability': 'Blaze',
        'Description': 'If HP is ≤ 1/3 of total, then Fire type moves are 50% more powerful.'
        }

cacophony = {
        'Ability': 'Cacophony',
        'Description': 'Avoids sound-based moves.'
        }

clorophyll = {
        'Ability': 'Clorophyll',
        'Description': 'During harsh sunlight, doubles the speed.'
        }

clear_body = {
        'Ability': 'Clear Body',
        'Description': 'Prevents stat reduction from opposing pokemon.\nThe exceptions are self-inflicted reductions from moves like curse or superpower.\nThis ability is ignored by moves and abilities that ignore abilities, such as Mold Breaker.'
        }

cloud_nine = {
        'Ability': 'Cloud Nine',
        'Description': 'Negates all effects of weather, though the weather itself does not disappear.'
        }

color_change = {
        'Ability': 'Color Change',
        'Description': 'When hit by an attack, this pokemon changes its type to that of the move it is hit with.\nIt does not change if hit by Struggle. Nor does it change if its substitute is hit. The ability activates after the first hit of a multi-hit move, but after status-infliction. (E.g.: it can still be poisoned by poison sting before it becomes poison.'
        }

compound_eyes = {
        'Ability': 'Compound Eyes',
        'Description': 'Raises accuracy of moves by 30%.'
        }

cute_charm = {
        'Ability': 'Cute Charm',
        'Description': 'When the pokemon with the ability is hit by a contact-move, there is a 30% chance that the attacker will become infatuated if it is of the opposite gender. It will not activate on same-sex or sexless pokemon. For multi-hit moves that make contact, each hit has an independent chance to activate the ability.'
        }

damp = {
        'Ability': 'Damp',
        'Description': 'Prevents self-destruction moves, such as Self-Destruct or Explosion. If a pokemon attempts to use one of those moves in battle with a pokemon with this ability, then the move will fail and the user will not faint or take damage. It also prevents damage from the Aftermath ability.'
        }

drizzle = {
        'Ability': 'Drizzle',
        'Description': 'Once the pokemon with this ability enters battle, it starts to rain. The rain persists unless another pokemon changes it, through either an ability such as Air Lock or Drought, or through a move such as Sunny Day. If a pokemon with Drizzle is put into battle on the same turn as a pokemon with a weather-changing ability such as Drought, then the ability of the slower pokemon will override the ability of the faster pokemon.'
        }

drought = {
        'Ability': 'Drought',
        'Description': 'When a pokemon with this ability is switched into battle, harsh sunlight shines down from above (a la Sunny Day). The harsh sunlight persists unless another pokemon changes it, through either an ability such as Air Lock or Drizzle, or through a move such as Rain Dance. If a pokemon with Drought is put into battle on the same turn as a pokemon with a weather-changing ability such as Drizzle, then the ability of the slower pokemon will override the ability of the faster pokemon.'
        }

early_bird = {
        'Ability': 'Early Bird',
        'Description': 'Wake up from Sleep faster. For example, if the number of turns to sleep is 6, it will instead be halved to 3. If it is 3 turns, it will be rounded to 1 turn. If it is 1 turn, the pokemon will instantly wake up. This applies to self-inducing sleep moves, such as Rest.'
        }

effect_spore = {
        'Ability': 'Effect Spore',
        'Description': 'When a pokemon with this ability is hit by a contact move, there is a 30% chance that the attacker will be affected with a status. \n30% chance to be poisoned, paralyzed, or asleep.\n9% chance of poison.\n10% chance of paralysis.\n11% chance of sleep.\nThis ability cannot poison Poison-types or Steel-types, nor can it paralyze Electric-types. If the pokemon with this ability is hit by a multi-hit contact move, each hit has an independent chance to activate the ability.'
        }

flame_body = {
        'Ability': 'Flame Body', 
        'Description': 'When a pokemon with this ability is hit by a contact move, there is a 30% chance that the attacker will be burned. If a pokemon with this ability is hit by a multi-hit contact move, then each hit has an independent chance to activate this ability.'
        }

flash_fire = {
        'Ability': 'Flash Fire', 
        'Description': 'Grants immunity to Fire attacks. When hit by a Fire-type move, this ability activates. Once it is activated, the power of Fire-type moves is increased by 50%. Subsequent hits from Fire-type moves do not grand additional power, but the immunity remains. The ability will not activate if the pokemon is protected from the move, nor will it activate while the pokemon with the ability is frozen.'
        }

forecast = {
        'Ability': 'Forecast',
        'Description': 'The pokemon changes its form and type depending on the weather.\nHarsh sunlight turns it into a Fire-type with its Sunny Form.\nDuring Hail, it becomes Ice-type with its Snowy Form.\nDuring Rain, it will become Water-type with its Rainy Form.\nDuring a sandstorm, it will revert to its normal form as a Normal type. It will also revert to its normal form if a pokemon on the field has Cloud Nine or Air Lock.\nThis ability has no effect on pokemon other than Casterform. The ability does not change type and form until after Stealth Rock deals damage.\nIf somehow the pokemon with this ability loses its ability, it will be stuck in its current form and change form to match the weather if it regains Forecast. The ability can be copied by Role Play and Trace.'
        }

guts = {
        'Ability': 'Guts',
        'Description': "It's so gutsy that having a status condition boosts the Pokémon's Attack stat by 50%. Being burnt doesn't cut the strength either.\n*Gens3-5: The attack boost activates if the pokemon is frozen and uses a move that thaws itself out, like Flame Wheel or Flare Blitz.\n* Gen6: The attack boost doesn't activate if the pokemon thaws itself out using a move like Flame Wheel or Flare Blitz."
        }

huge_power = {
        'Ability': 'Huge Power',
        'Description': 'Doubles the Attack stat of the pokemon with this ability.'
        }

hustle = {
        'Ability': 'Hustle',
        'Description': 'Increases attack stat by 50%, but lowers the accuracy of physical moves by 20%. The accuracies of Special moves and Status moves are unaffected.'
        }

hyper_cutter = {
        'Ability': 'Hyper Cutter',
        'Description': 'Thanks to the big, meaty claws on the pokemon, it is too proud to have its Attack stat reduced by an opponent. The ability does not prevent the pokemon from reducing its own attack stat through moves like Superpower.'
        }

illuminate = {
        'Ability': 'Illuminate',
        'Description': 'This ability has no value in battle. Outside of battle, it increases the likelihood of encounters with wild Pokemon.'
        }

immunity = {
        'Ability': 'Immunity',
        'Description': 'Prevents poisoning. If a pokemon acquires this ability, they will not be cured of poison until after a pokemon takes its turn.'
        }

inner_focus = {
        'Ability': 'Inner Focus',
        'Description': 'The intense focus of this pokemon prevents it from flinching.'
        }

insomnia = {
        'Ability': 'Insomnia',
        'Description': 'This pokemon cannot sleep. Sleep-inducing moves do not affect it, nor does Yawn make it drowsy. Rest also fails.'
        }

intimidate = {
        'Ability': 'Intimidate',
        'Description': 'When this pokemon enters battle, it lowers the Attack stat of the opponent by one stage.'
        }

keen_eye = {
        'Ability': 'Keen Eye',
        'Description': 'Prevents other pokemon from lowering the Accuracy of this pokemon. Moves, effects, or abilities that decrease accuracy without stat stages, like Wonder Skin or Sand Veil, are unaffected by this ability.'
        }

levitate = {
        'Ability': 'Levitate',
        'Description': 'Ground moves cannot hit this pokemon. It is immune to the effects of Arena Trap, terrain, Spikes, Toxic Spikes, and Sticky Web.'
        }

lightning_rod = {
        'Ability': 'Lightning Rod',
        'Description': 'Draws electric moves that attack a single target to this pokemon. It cannot redirect Electric-type Hidden Power.'
        }

limber = {
        'Ability': 'Limber',
        'Description': 'This pokemon cannot be paralyzed'}

liquid_ooze = {
        'Ability': 'Liquid Ooze',
        'Description': 'HP-draining moves used on this pokemon deal damage to the user instead of sapping health. The amount of health that would have been restored by moves such as Giga Drain, Leech Life, or Leech Seed deal the amount of damage that would have ordinarily been restored. The damage dealt by the move is still inflicted.'
        }

magma_armor = {
        'Ability': 'Magma Armor',
        'Description': 'Prevents this pokemon from being frozen.'
        }

magnet_pull = {
        'Ability': 'Magnet Pull', 
        'Description': 'Prevents Steel-type opponents from switching out as long as this pokemon is in battle. Moves like Baton Pass or U-Turn will still allow the pokemon to switch out.'
        }

marvel_scale = {
        'Ability': 'Marvel Scale',
        'Description': "Thanks to this Pokémon's marvelous scales, if it has a status condition, the Defense stat is boosted by 50%."
        }

minus = {
        'Ability': 'Minus',
        'Description': 'This ability works in Double Battles. When it is in a Double Battle with a pokemon with the Plus ability, its Special Attack stat is boosted by 50%.'
        }

natural_cure = {
        'Ability': 'Natural Cure',
        'Description': 'When switching out of battle, this pokemon is cured of its status condition.'
        }

oblivious = {
        'Ability': 'Oblivious',
        'Description': 'This pokemon is immune to infatuation. Who said being dense was a bad thing?'
        }

overgrow = {
        'Ability': 'Overgrow',
        'Description': 'If HP is ≤ 1/3 of total, then Grass type moves are 50% more powerful.'
        }

own_tempo = {
        'Ability': 'Own Tempo',
        'Description': 'This pokemon cannot be confused, even by moves that inflict confusion on itself.'
        }

pickup = {
        'Ability': 'Pickup',
        'Description': 'No use in battle. Outside of battle, it has a chance of picking up stuff.'
        }

plus = {
        'Ability': 'Plus',
        'Description': 'This ability works in Double Battles. When it is in a Double Battle with a pokemon with the Minus ability, its Special Attack stat is boosted by 50%.'
        }

poison_point = {
        'Ability': 'Poison Point',
        'Description': 'When this pokemon is hit by a contact move, there is a 30% chance that the attacker will become poisoned. This ability does not affect Poison-type or Steel-type pokemon. If this pokemon is hit by a multi-hit contact move, then each hit has an independent chance to activate the ability.'
        }

pressure = {
        'Ability': 'Pressure',
        'Description': 'When attacking this pokemon, the opponent uses one additional PP when moving, regardless of of whether it hits or not.'
        }

pure_power = {
        'Ability': 'Pure Power',
        'Description': 'Doubles the Attack stat of this pokemon.'
        }
rain_dish = {
        'Ability': 'Rain Dish',
        'Description': 'During rain, this pokemon regains 1/16 of its maximum health per turn.'
        }

rock_head = {
        'Ability': 'Rock Head',
        'Description': 'This pokemon is unaffected by the recoil from moves like Double-Edge. Struggle still deals damage. Also, damage is still taken if Jump Kick or High-Jump Kick miss.'
        }

rough_skin = {
        'Ability': 'Rough Skin',
        'Description': 'When this pokemon is hit with a contact move, the attacker takes damage equal to 1/16 of its own max HP. If this pokemon is hit by a multi-hit contact move, each hit activates this ability.'
        }

run_away = {
        'Ability': 'Run Away',
        'Description': 'This pokemon can always run away from random encounters. It has no effect on switching out of battle.'
        }

#%%
ability_list = [air_lock, arena_trap, battle_armor, blaze, cacophony,
                clorophyll, clear_body, cloud_nine, color_change, compound_eyes,
                cute_charm, damp, drizzle, drought, early_bird, effect_spore, 
                flame_body, flash_fire, forecast, guts, huge_power, hustle, 
                hyper_cutter, illuminate, immunity, inner_focus, insomnia, 
                intimidate, keen_eye, levitate, lightning_rod, limber, 
                liquid_ooze, magma_armor, magnet_pull, marvel_scale, minus, 
                natural_cure, oblivious, overgrow, oblivious, pickup, plus, 
                poison_point, pressure, pure_power, rain_dish, rock_head, 
                rough_skin, run_away
                
                ]

#%%
def make_pickles(ls = ability_list):
    for itm in ls:
        with open('abilities/' + itm['Ability'] + '.pickle', 'wb') as output_file:
            pickle.dump(itm, output_file)
        
#%%
print('List of Abilities, sorted alphabetically:')
letter = 'A'
print('A')
for ind,val in enumerate(ability_list):
    if val['Ability'][0] != letter:
        letter = val['Ability'][0]
        print(letter)
    print('\t',ind, val['Ability'])