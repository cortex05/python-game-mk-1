# Initial attempt to recreate and then improve role playing project

# Import enemy and hero data
# import necessary functions in java

# MAIN FUNCTION START

player = {
  "player_name": None,
  "player_class": None
}

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
# player changed to result of initial_config
  # INITIAL CONFIG METHOD (Accept player as value)

    # scanner?
player_finished = False
player_name = input("What is your name?\n")
player["player_name"] = player_name
    # MAKE LOOP
print(f"\nHello {player['player_name']}")
while True:
  character_choice = input('''
    Please Select your class
    1) Elf
    2) Dwarf
    3) Swordsman
    4) Quit
    \n''')

  # selection check
  if character_choice == '1' or character_choice == '2' or character_choice == '3':
    proto_selection = descriptions[int(character_choice) - 1]
    selection = input(f'''\nYou choose {proto_selection["name"]}. \n \n{proto_selection["name"]} is {proto_selection["description"]}. \n \nDo you wish this to be your character? Y/N \n''')
    if selection.lower() == 'y':
      print(f'Congrats on picking {proto_selection["name"]}\n')
      break
    else:
      continue
  elif character_choice == '4':
    print("Goodbye")
    break
  else:
    print("Please enter a number\n")
    continue  
  
 

      # for each selection, explain their skills, ask for confirmation, (if not repeat), 
      # if yes, set finished to true
  # END INITIAL CONFIG

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