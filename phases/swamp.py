import os
from Player import Player
from directions import nav_options, swamp_coordinates
from utility.battle_functions import battle_launch
from utility.nav_functions import navigation_options, reverse_step


def swamp_loop(player: Player):
    is_running = True
    moving_coords = [2, 1]
    last_command = None
    bridge_unlock = False
    first_unlock = True

    while is_running:
        os.system('cls')
        print(f'Last command: {last_command}')
        print(f'Moving coords: {moving_coords}')
        holder = swamp_coordinates.grid[moving_coords[0]][moving_coords[1]]

        if 'alt_pathway' in holder and holder['alt_pathway'] and player.inventory and 'CASTLE_GATE' in player.inventory:
            # condition check for if text has gone?
            location = swamp_coordinates.grid[moving_coords[0]][moving_coords[1]]['alt_pathway']
            bridge_unlock = True
        else:
            location = swamp_coordinates.grid[moving_coords[0]][moving_coords[1]]

        if location['random_battle']:
            result = battle_launch(player, location['unlock_value'])
            if result == 'LOSE':
                is_running: False
                break
            elif result == 'RETREAT':
                reverse_step(last_command, moving_coords)
                continue

        if bridge_unlock and first_unlock:
            print(location['alt_description'])
            first_unlock = False
        else:
            print(location['description'])
        

        text_options = ''
        choice_options = []
        for option in location["options"]:
            text_options = text_options + nav_options.nav_options[option]
            choice_options.append(option)

        print(f'Options: {choice_options}')
        choice = input(text_options)
    
        if choice:
            if int(choice):
                int_choice = int(choice)
            else:
                print('Enter a valid option')
                continue
        else:
            print('Enter a valid option')
            # Need validation for bad input to NOT do random encounter again.
            continue

        last_command = navigation_options(int_choice, choice_options, moving_coords)
