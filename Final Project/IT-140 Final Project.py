# Author: Caleb Smith
# Date: 10.13.2023

# This project focuses on creating a text-based adventure game

# Introduce the player to the game and show them the movement and item commands

def intro():
    print(
        
          '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n'
          '*                                                                                                 *\n'
          '*   You are an undercover NATO spy. You have been stationed in East Germany for 18 months.        *\n'
          '*   Your rotation is over, but your handler has given you another task on your way out.           *\n'
          '*   1. Find the underground radio office in a clandestine East German tunnel.                     *\n'
          '*   2. Inside the office, locate and steal the KGB radio code book that was released this week.   *\n'
          '*                                                                                                 *\n'
          '*   ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||      *\n'
          '*                                                                                                 *\n'
          '*   You entered a hole in a fence outside of Micro District #27 during a 5AM guard change.        *\n'
          '*   You were able to see the Wall faintly through the morning fog on your way to the tunnel.      *\n'
          '*   You crawl your way inside the dark tunnel entrance and feel an opening in front of you.       *\n'
          '*                                                                                                 *\n'
          '*   ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||      *\n'
          '*                                                                                                 *\n'
          '*   Just in case you have forgotten your training, Agent Python, here is a refresher.             *\n'
          '*                                                                                                 *\n'
          '*   To move enter: | "north" | "south" | "east" | "west" | to move in that direction.             *\n'
          '*   If your move is valid, you move in that direction. If you enter an invalid move, try again.   *\n'
          '*   To surrender to the KGB, enter exit at any time, you coward.                                  *\n'
          '*                                                                                                 *\n'
          '*   Some rooms have items. You will need 6 items to make your escape.                             *\n'
          '*                                                                                                 *\n'
          '*   To pick up an item, enter: | "pick up" | and the item will be added to your backpack.         *\n'
          '*   In order to escape, you need all six items, otherwise, you will be compromised.               *\n'
          '*                                                                                                 *\n'
          '*   ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||      *\n'
          '*                                                                                                 *\n'
          '*   Lastly, keep your eyes out for any rouge KGB agents in the tunnel.                            *\n'
          '*   Signals intelligence suggests there is a missing high-ranking agent who was last seen         *\n'
          '*   ... in the tunnels ...                                                                        *\n'
          '*   Be safe Agent Python, you are almost home.                                                    *\n'
          '*                                                                                                 *\n'
          '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\n\n'

          )

# Show the player the item on the ground in the corresponding room
# Then, take an input from them about what they do with the item


def items():
    if 'item' in rooms_and_items[current_room].keys():
        ground_item = rooms_and_items[current_room]["item"]
      
        # If the room has an item, and it's not in the player's backpack, tell the player the item is available
      
        if ground_item not in backpack:
            print(f'\nYou see {ground_item} on the ground. What do you do?\n')
          
            # Take input from the player, looking got for them to pick up the item or anything else (skip)
          
            pick_up_item = input(str())
          
            # If the player picks up the item, add it to their inventory, otherwise, don't
          
            if pick_up_item == 'pick up':
                backpack.append(rooms_and_items[current_room]['item'])
                return
            else:
                return
              
        # If the room has an item, and it is in the player's backpack, skip the inventory addition process
      
        elif ground_item in backpack:
            return

# Print the boss fight story based on the player's inventory having six items (win) or fewer (loss)


def boss_fight():
    # Print the boss fight lore
  
    print("You make your way to the tunnel exit.")
    print("There is a tiny ray of light visible in one corner of the room.")
    print("Suddenly the light is gone.")
    print("You pull out your flashlight, then a bright light appears...")
    print("You see a KGB agent holding a flashlight dressed in an all plaid KGB uniform.")
    print('The figure says: "Agent Python... you are not so stealthy.')
    print('I am agent Plaidimir Vutin and I am here to stop you.')
  
    # Print the winning story if the player wins (has all 6 items)
  
    if len(backpack) >= 6:
        print("\n\n\nYou hear a loud noise, suddenly 6 CIA agents drop into the tunnel.")
        print("They quickly subdue Plaid and greet you.")
        print('"Welcome back Agent Python. Thanks for getting the code book for us."')
        print('"It is time for you to rest stateside. Then we have another mission for you.')
        print('"Something about some about taking down some company called zyBooks."')
        print('"Anyway, we gotta get out of here."')
        print("Congratulations Agent Python! You win!")
      
    # Print the losing story if the player loses (fewer than 6 items)
  
    elif len(backpack) < 6:
        print("\n\n\nYou hear a loud noise, suddenly 6 KGB agents drop into the tunnel.")
        print("You are no match.")
        print("You surrender.")
        print("You have failed. You need all 6 items to escape.")
        print("GAME OVER.")

# A dictionary that links a room to other rooms and includes the item in the room


rooms_and_items = {
    'Tunnel Entrance': {'North': 'First Hall'},
    'First Hall': {'North': 'Open Area', 'South': 'Tunnel Entrance', 'item': 'an Office key'},
    'Open Area': {'North': 'Second Hall', 'South': 'First Hall', 'East': 'Office', 'item': 'a newspaper'},
    'Office': {'West': 'Open Area', 'item': 'the radio code book'},
    'Second Hall': {'West': 'Bend', 'South': 'Open Area', 'item': 'batteries'},
    'Bend': {'East': 'Hall 2', 'North': 'Third Hall', 'item': 'a radio'},
    'Third Hall': {'South': 'Bend', 'East': 'Tunnel Exit', 'item': 'a flashlight'},
    'Tunnel Exit': {'West': 'Third Hall'}
}

# Create an inventory for the player & remove articles before items used in messages

backpack = []  # Spent so long trying to format the backpack to exclude articles, eventually gave up for time reasons

# Call the intro function

intro()

# Start the player in the Tunnel Entrance & pass that to the current room variable

start_room = 'Tunnel Entrance'
current_room = start_room

# Create a constant game loop

while True:
  
    # Tell the player what room they are in
  
    print(f'\nYou are in the {current_room}.')

    # Call the item function
  
    items()
  
    # Display the player's inventory unless they are in the starting room
  
    if current_room != 'Tunnel Entrance':
        print(f'\n Your backpack: {backpack}')

    # Take a movement input from the player & split the input into a list
  
    move = input('\nEnter a move: ').split()[-1].capitalize()
  
    # Print a divider
  
    print('\n||||||||||||||||||||||||||||||||||||||||||||||||\n')

    # Accept a possible move & change the player's current room
  
    if move in rooms_and_items[current_room]:
      
        current_room = rooms_and_items[current_room][move]
      
    # Allow the player to exit by typing 'Exit' & exit the loop
  
    elif move == 'Exit':
        print("Game Over. \nThanks for playing!!")
        break
      
    # Tell the player they entered an invalid move & go back to the top of the loop
  
    else:
        print('\nInvalid move, Agent. Pull yourself together!\nTry again.\n')
        print('\n||||||||||||||||||||||||||||||||||||||||||||||||\n')

        items()

    # Call the boss fight function when the player is in the tunnel entrance
  
    if current_room == 'Tunnel Exit':
        boss_fight()
        break
