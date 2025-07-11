from characters import Elf, Dwarf, Swordsman
from threading import Timer
import os

# Set Name


def setPlayerName():
    player_name = input("Please enter your name.\n")

    os.system('cls')
    print(f"\nHello {player_name}")

    return player_name


# Initialization
descriptions = [
    {
        "name": "Elf",
        "description": '''a woodland sprite who moves fast and uses magic.'''
    },
    {
        "name": "Dwarf",
        "description": '''a sturdy, slow-moving tank.'''
    },
    {
        "name": "Swordsman",
        "description": '''a well balanced fighter.'''
    },
]


def initialiationLoop(name):
    player = ''
    while True:
        try:
            character_choice = int(input('''
        Please Select your class
        1) Elf
        2) Dwarf
        3) Swordsman
        4) Quit
      \n'''))

            if character_choice == 1:
                proto_selection = descriptions[character_choice - 1]
                selection = input(
                    f'''\nYou choose {proto_selection["name"]}. \n \n{proto_selection["name"]} is {proto_selection["description"]}. \n \nDo you wish this to be your character? Y/N \n''')
                if selection.lower() == 'y':
                    player = Elf.Elf(name)
                    break
                else:
                    os.system('cls')
                    continue
            elif character_choice == 2:
                proto_selection = descriptions[int(character_choice) - 1]
                selection = input(
                    f'''\nYou choose {proto_selection["name"]}. \n \n{proto_selection["name"]} is {proto_selection["description"]}. \n \nDo you wish this to be your character? Y/N \n''')
                if selection.lower() == 'y':
                    player = Dwarf.Dwarf(name)
                    break
                else:
                    os.system('cls')
                    continue
            elif character_choice == 3:
                proto_selection = descriptions[int(character_choice) - 1]
                selection = input(
                    f'''\nYou choose {proto_selection["name"]}. \n \n{proto_selection["name"]} is {proto_selection["description"]}. \n \nDo you wish this to be your character? Y/N \n''')
                if selection.lower() == 'y':
                    player = Swordsman.Swordsman(name)
                    break
                else:
                    os.system('cls')
                    continue
            elif character_choice == 4:
                print("Goodbye")
                return
                # break
            else:
                os.system('cls')
                print("Please enter a whole number between 0 and 5\n")
                continue

        except ValueError:
            os.system('cls')
            print("Please enter a number")
        continue

    return player

# Intro scroll


def introScroll(name: str):
    introScrollText = [
        f'Hello {name}. this is the intro scroll.',
        'You are starting on an adventure.',
        'You have to fight through a swamp, cross a moat and enter a castle.',
        'After that, you must find the princess somewhere in the castle.',
        'Take heart, do not despair and step out with determination!'
    ]
    os.system('cls')
    for text in introScrollText:
        input(f'{text} \n')
    os.system('cls')
