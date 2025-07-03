import characters

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
        selection = input(f'''\nYou choose {proto_selection["name"]}. \n \n{proto_selection["name"]} is {proto_selection["description"]}. \n \nDo you wish this to be your character? Y/N \n''')
        if selection.lower() == 'y':
          player = characters.Elf.Elf(name)
          break
        else:
          continue
      elif  character_choice == 2:
        proto_selection = descriptions[int(character_choice) - 1]
        selection = input(f'''\nYou choose {proto_selection["name"]}. \n \n{proto_selection["name"]} is {proto_selection["description"]}. \n \nDo you wish this to be your character? Y/N \n''')
        if selection.lower() == 'y':
          player = characters.Dwarf.Dwarf(name)
          break
        else:
          continue
      elif  character_choice == 3:
        proto_selection = descriptions[int(character_choice) - 1]
        selection = input(f'''\nYou choose {proto_selection["name"]}. \n \n{proto_selection["name"]} is {proto_selection["description"]}. \n \nDo you wish this to be your character? Y/N \n''')
        if selection.lower() == 'y':
          player = characters.Swordsman.Swordsman(name)
          break
        else:
          continue
      elif character_choice == 4:
        print("Goodbye")
        break
      else:
        print("Please enter a whole number between 0 and 5\n")
        continue  

    except ValueError:
      print("Please enter a number")
    continue
      
  return player
