# Initial attempt to recreate and then improve role playing project

# import necessary functions in java

# MAIN FUNCTION START

# CHANGE THIS TO IMPORT
class Player:
  total_experience = 0
  base_level = 1000
  to_next_level = 1000

  num_health_potions = 4
  health_potion_heal_amount = 30
  health_potion_drop_dhance = 50; # 50 Percent chance to drop a health potion
  # levelUpChance = 50 - Don't know about this...

class Swordsman(Player):
  player_class = "Swordsman"
  standard_attack = "Slash"
  special_attack = "Overhead Smash"
  heavy_attack = "Thrust"
  description = '''a well balanced fighter.'''
  def __init__(self, name):
    self.name = name
    print(f"\nSwordsman Selected! Hack and slash it is. Congrats {name}!\n\n\n")

class Elf(Player):
  player_class = "Elf"
  standard_attack = "Swipes"
  special_attack = "Precision Arrow"
  heavy_attack = "Drop Kick"
  description = '''a well balanced fighter.'''

  health = 70
  baseHealth = 70
  strength = 18
  defense = 18
  agility = 40
  def __init__(self, name):
    self.name = name
    print(f"\nElf Selected! Quick and nimble is the way. Congrats {name}!\n\n\n")    

class Dwarf(Player):
  player_class = "Dwarf"
  standard_attack = "Slash"
  special_attack = "Earth shaker"
  heavy_attack = "Guillotine"
  description = '''a well balanced fighter.'''

  health = 120
  baseHealth = 120
  strength = 50
  defense = 30
  agility = 15
  def __init__(self, name):
    self.name = name
    print(f"\nDwarf Selected! Heavy hitter I see. Congrats {name}!\n\n\n")

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
    character_choice = input('''
    Please Select your class
    1) Elf
    2) Dwarf
    3) Swordsman
    4) Quit
    \n''')

  # selection check
    if character_choice == '1':
      proto_selection = descriptions[int(character_choice) - 1]
      selection = input(f'''\nYou choose {proto_selection["name"]}. \n \n{proto_selection["name"]} is {proto_selection["description"]}. \n \nDo you wish this to be your character? Y/N \n''')
      if selection.lower() == 'y':
        player = Elf(name)
        break
      else:
        continue
    elif  character_choice == '2':
      proto_selection = descriptions[int(character_choice) - 1]
      selection = input(f'''\nYou choose {proto_selection["name"]}. \n \n{proto_selection["name"]} is {proto_selection["description"]}. \n \nDo you wish this to be your character? Y/N \n''')
      if selection.lower() == 'y':
        player = Dwarf(name)
        break
      else:
        continue
    elif  character_choice == '3':
      proto_selection = descriptions[int(character_choice) - 1]
      selection = input(f'''\nYou choose {proto_selection["name"]}. \n \n{proto_selection["name"]} is {proto_selection["description"]}. \n \nDo you wish this to be your character? Y/N \n''')
      if selection.lower() == 'y':
        player = Swordsman(name)
        break
      else:
        continue
    elif character_choice == '4':
      print("Goodbye")
      break
    else:
      print("Please enter a valid number\n")
      continue  

  return player
  # if yes, set finished to true
  # END INITIAL CONFIG


player = initialiationLoop(player_name)
print(player.standard_attack)
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