import os
from directions import nav_options, swamp_coordinates
from utility.nav_functions import navigation_options

moving_coords = [2, 1]

while True:
    os.system('cls')
    print(f'Moving coords: {moving_coords}')
    location = swamp_coordinates.grid[moving_coords[0]][moving_coords[1]]
    print(location["description"])

    if location['random_battle']:
        input('Battle Loop!')

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

    navigation_options(int_choice, choice_options, moving_coords)
