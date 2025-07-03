# Initial attempt to recreate and then improve role playing project

# import necessary functions in java
import characters
# MAIN FUNCTION START

# CHANGE THIS TO IMPORT

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
# END IMPORT SECTION
# INITIAL CONFIG METHOD (Accept player as value)

player_finished = False
player_name = input("Please enter your name.\n")

print(f"\nHello {player_name}")

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


player = initialiationLoop(player_name)

if player == '':
  player_finished = True


# Do intro scroll 
  # INTRO SCROLL METHOD
    # initialize name
    # give the spiel
  # END SWAMP LOOP

# start sawmp loop
  # START LOOP METHOD ( player as argument)
    # isRunning Boolean
    # Initial position variables
    # Call swampOptions with "start" and position variables
    # Loop while "isRunning"
  
    # END OF ORIGINAL
      # PLANS
        # PART 1
        # Have 4 sections that involve navigation
        # --swamp, gate, mordor, baradur
        # Have random battles with level up mechanic
        # --progressive difficulty
        # Final Boss
        # --special features?

        # PART 2
        # Inventory
        # --WEAPONS and armor
        # Locations that have buttons
        # --Button opens up switch
  # END SWAMP LOOP METHOD

  #START SWAMP OPTIONS FUNCTION ## APPEARS TO BE GENERAL NAVIGATION
    #  start loop from start position
    #         System.out.println("1 - Proceed North");
    #         System.out.println("2 - Proceed West");
    #         System.out.println("3 - Proceed East");

    #         String option = in.nextLine();

    #         if(option.equalsIgnoreCase("1")){
    #             System.out.println("You proceed North");
    #             yAxis = yAxis + 1;
    #             System.out.println(yAxis);
    #         } else if (option.equalsIgnoreCase("2")){
    #             System.out.println("You Proceed west");
    #             xAxis--;
    #         } else if(option.equalsIgnoreCase("3")){
    #             System.out.println("You proceed east");
    #             xAxis++;
    #         } else {
    #             System.out.println("Try again");
    #             swampOptions("start", yAxis, xAxis);
    #         }