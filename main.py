# Initial attempt to recreate and then improve role playing project

# Import enemy and hero data
#import necessary functions in java

# MAIN FUNCTION START

# Make player variable from HERO type, set type to null
# player changed to result of initial_config
  # INITIAL CONFIG METHOD (Accept player as value)

    # scanner?
    # boolean finished = false
    # ask for name, input
    # MAKE LOOP
      # Say Hello
      # ask for class, offer options for characters or quit
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
    #  if(position.equals("start")){
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
    #     }

