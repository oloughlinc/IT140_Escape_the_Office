# Purpose: A text based game in which the player will navigate through a dungeon environment. Player will
# be able to pick up objects and will win if they can get all the objects while avoiding the enemy who lives
# in a certain room.
#
# Contraints: User may enter any text. Expecting a command and a direction (go north etc..)
#
# Expected Results: Program will display information through text depending on which room the user is in. It
# will keep track of the items that the user has picked up. Game will end if the user types 'exit', if all items
# have been gathered, or if the user meets the enemy.
#
# Version   Author      Date        Desc
# 1         Craig O.    8/7/21      Initial version

# ------------------------------------------------------------------------------------------------

room_details = {
        'Main Office': "\nA sea of desks, an open office concept where everyone avoids eye contact.\n"
                       "The lighting is white that feels too blue, the air conditioner is\n"
                       "set just a few degrees colder than anyone actually wants, and the whole\n"
                       "space hums quietly while everyone works in silence.\n",
        'Supply Closet': "\nA dimly lit back room with shelves that are mostly empty. In the back\n"
                         "of the space sits a gray cabinet with a lock. You briefly wonder about it\n"
                         "then remember that your favorite pen at home just ran out of ink.\n",
        'Back Office': "\nEven colder than the Main Office. This is where The Engineers work,\n"
                       "away from the light. A pale, sullen man looks up quizzically through you, then\n"
                       "back down to his slide ruler. You move as quietly as possible as you continue\n"
                       "your quest.\n",
        'Front Lobby': "\nA glassy ceramic floor with a few tasteful but uncomfortable chairs set around\n"
                       "a table with magazines from five years ago scattered on top.\n"
                       "A picture of a large, grinning, man with a imposing wave of black,\n"
                       "swept back hair on his head hangs in the wall. The eyes seem to follow you.\n"
                       "You shudder as you tiptoe over the hard floor surface.\n",
        'Bathroom': "\nNeutral colors and some cracked floor tiles. One faucet drips slowly.\n"
                    "You sometimes imagine the large, brightly lit mirrors over the sink are one way,\n"
                    "and hide some shadowy (probably corporate) figure who watches you like their experiment.\n"
                    "Someone sobs in the last stall.\n",
        'Break Room': "\nYou see the type of large, perfectly circular tables that must only exist in office\n"
                      "break rooms. Vending machines line the back wall, and a sink with the sponge that\n"
                      "nobody uses but is somehow well worn.\n",
        'Courtyard': "\nA few flowers in pots and an atrium of glass. You look up briefly as a bird flies past,\n"
                     "and a backdrop of the fluffiest, whitest clouds any day can produce. It really must be quite\n"
                     "nice out, you think to yourself. You imagine the cool breeze, and focus on the task\n"
                     "at hand.\n",
        'Executive Office': '',
}


def display_instructions():
    '''print instructions on playing the game'''
    print()
    print("Collect all 6 of your missing items in order to win. Encounter your boss, however,\n"
          "and it is back to work for you!\n")
    print("Available commands:\n")
    print("Moving character: go North, go South, go East, go West")
    print("Grabbing an item: get 'item name'")
    print("Quit at any time with 'exit'. Type 'help' to display these instructions again.")


def print_room_details(rooms, current_room):
    '''Prints the current room, details about that room, player's inventory, and any item in the room'''
    print()
    print(f"You are in the {current_room}.")
    print(f"{room_details[current_room]}")
    print("Inventory: ", player_inventory)

    if rooms[current_room]['item'] is None:
        pass
    else:
        print(f"You see your {rooms[current_room]['item']}")


def move(direction, rooms, current_room):
    '''returns the room in the direction chosen from the current room'''
    if direction in rooms[current_room]:

        new_room = rooms[current_room][direction]
        return new_room

    else:

        print("\nYou can't go that way!")
        return current_room


def get_item(item, rooms, current_room):
    '''given an item and the rooms dict, will check for the item in the room. If item exists,
    remove from the room and add to the inventory'''
    if rooms[current_room]['item'] == item:
        print(f"{rooms[current_room]['item']} retrieved!")
        player_inventory.append(rooms[current_room]['item'])
        rooms[current_room]['item'] = None
    else:
        print(f"Can't get {item}!")


def game_lost():
    print("\nThe air goes cold around you. Across the room, at his desk, a large man\n"
          "watches, one eye closed. He lets out a snore, then, slowly, a grunt of realization.\n"
          "You try to remain as still as the floor beneath you, with every bit of effort,\n"
          "to become somehow transparent.. but it is no use.\n You are caught.\n\n"
          "The large man behind the desk slowly labors to his feet.\n"
          "\"And where do you think YOU'RE going\", your boss articulates with great effort from the chest\n"
          "beneath his too expensive suit. You slink back to your desk without a word.\n"
          "Outside the birds are singing and the wind is blowing through the leaves of the last\n"
          "perfect day of summer.")
    print('\nTHE END')


def game_won():
    print("\nThat's it! This must be everything you came into work with! Well, everything you\n"
          "can remember. The rest is not important you think, your window of opportunity\n"
          "must be closing soon, and it is time to go.\n\n"
          "You begin to casually head towards the exit, no big deal. Your coworkers are a mix of\n"
          "general disinterest and sullen faces illuminated by screens. By the time you are near the exit\n"
          "your casual pace has become nearly a sprint.\n\n"
          "You make it to the exit! The picture of your boss on the wall remains smiling as you leave.\n\n"
          "You drive the long way out of the parking lot, avoiding the large windows of your boss'\n"
          "executive office. The weekend awaits! In your rear view mirror, the office building stands,\n"
          "waiting patiently for Monday.")
    print("\nYOU WON!!")


def main():
    '''contains the main game loop, input checking, and win loss condition check'''

    # Map of the dungeon layout. Each room contains a reference to available directions
    # and an item to be acquired. One room contains the villain as an item.
    rooms = {
        'Main Office': {'North': 'Back Office', 'South': 'Front Lobby', 'East': 'Break Room',
                        'West': 'Supply Closet', 'item': None},
        'Supply Closet': {'East': 'Main Office', 'item': 'Pens'},
        'Back Office': {'East': 'Executive Office', 'South': 'Main Office', 'item': 'Hat'},
        'Front Lobby': {'North': 'Main Office', 'East': 'Bathroom', 'item': 'Keys'},
        'Bathroom': {'West': 'Front Lobby', 'item': 'Watch'},
        'Break Room': {'North': 'Courtyard', 'West': 'Main Office', 'item': 'Lunch'},
        'Courtyard': {'North': 'Executive Office', 'South': 'Break Room', 'item': 'Sunglasses'},
        'Executive Office': {'item': 'Boss!'}
    }

    # Text which will be displayed in case of invalid input
    invalid_input_text = "\nInvalid input! (type 'help' for details.)"

    # Set the starting room for the player
    current_room = 'Main Office'

    # ---------------------------------BEGIN GAME LOOP---------------------------
    playing = True
    while playing:

        print_room_details(rooms, current_room)

        # Check the win condition:
        if len(player_inventory) == 6:
            game_won()
            playing = False
            continue

        # Check the loss condition
        elif rooms[current_room]['item'] == 'Boss!':
            game_lost()
            playing = False
            continue

        # If player has not won or lost, get the next move
        else:
            print("-" * 80)
            user_move = input("Enter your move: ").capitalize()  # get user input for a move.
            # capitalize each 1st letter

        # general check that a user has not entered something excessively long that may break the code
        if len(user_move) > 15:
            print(invalid_input_text)
            continue  # Moves immediately to next iteration of game loop, foregoing the rest of the checks

        # checking input for the go or get command and making sure a valid direction is given
        input_tokens = user_move.split()
        if len(input_tokens) == 2:  # valid command input has two words only
            command, direction_or_item = input_tokens[:2]
            direction_or_item = direction_or_item.capitalize()
            if command == 'Go' and direction_or_item in ['North', 'South', 'East', 'West']:
                current_room = move(direction_or_item, rooms, current_room)  # CHANGE ROOMS
            elif command == 'Get':
                get_item(direction_or_item, rooms, current_room)  # ADD ITEM
            else:
                print(invalid_input_text)

        elif user_move == 'Exit':
            break

        elif user_move == 'Help':
            display_instructions()

        else:
            print(invalid_input_text)

    # Runs after loop condition is broken (playing = False)
    # If player has won or lost, keep the window open so they may see the win or loss text
    else:
        input("\nPress enter to exit")


# -------------------------Initialize game---------------------------------------

print("Welcome to Escape the Office!")
display_instructions()
player_inventory = []
main()