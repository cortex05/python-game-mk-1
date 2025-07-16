import os
from Player import Player
from directions import nav_options, swamp_coordinates
from utility.battle_functions import battle_launch
from utility.nav_functions import navigation_options, reverse_step


def swamp_loop(player: Player):
    is_running = True
    moving_coords = [2, 1]
    last_command = None

    while is_running:
        os.system('cls')
        print(f'Last command: {last_command}')
        print(f'Moving coords: {moving_coords}')
        location = swamp_coordinates.grid[moving_coords[0]][moving_coords[1]]

        if location['random_battle']:
            result = battle_launch(player)
            if result == 'LOSE':
                is_running: False
                break
            elif result == 'RETREAT':
                reverse_step(last_command, moving_coords)
                continue

        print(location["description"])

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
            continue

        last_command = navigation_options(int_choice, choice_options, moving_coords)
