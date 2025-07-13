import os
from directions import nav_options, swamp_coordinates

moving_coords = [2, 1]

while True:

    os.system('cls')
    print(f'Moving coords: {moving_coords}')
    location = swamp_coordinates.grid[moving_coords[0]][moving_coords[1]]
    print(location["description"])
    # print(location["options"])
    text_options = ''
    choice_options = []
    for option in location["options"]:
        text_options = text_options + nav_options.nav_options[option]
        choice_options.append(option)

    # print(f'Choice options: {choice_options}')

    choice = int(input(text_options))

    if choice == 1:
        moving_coords[0] = moving_coords[0] - 1
    elif choice == 2:
        moving_coords[1] = moving_coords[1] + 1
    elif choice == 3:
        moving_coords[0] = moving_coords[0] + 1
    elif choice == 4:
        moving_coords[1] = moving_coords[1] - 1