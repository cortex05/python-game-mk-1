def navigation_options(target: int, actual_options: list, moving_coords: list):
    choice = target -1
    print(f'Modded :{choice}')
    
    if choice in actual_options:
        if target == 1:
            moving_coords[0] = moving_coords[0] - 1
        elif target == 2:
            moving_coords[1] = moving_coords[1] + 1
        elif target == 3:
            moving_coords[0] = moving_coords[0] + 1
        elif target == 4:
            moving_coords[1] = moving_coords[1] - 1
    else:
        input("Please pick a valid option. Press enter to continue")