from room import Room
from player import Player
from item import Item

# Declare all the rooms

## ITEMS

outside_items = [Item('Sword', 'A Rusty old sword'), Item('Staff', 'Magical presence permeating around it')]
foyer_items = [Item('Key', 'It should open something')]
overlook_items = [Item('Potion', 'Can recover your health')]
narrow_items = [Item('Branch', 'A tree branch')]
treasure_items = [Item('Holy Grail', 'The Holy Grail')]

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", outside_items),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", foyer_items),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", overlook_items),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", narrow_items),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", treasure_items),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def move(command, name, current_player):

        if (command == "n"):
            player = Player(name, current_player.current_room.n_to)
            if (player.current_room != None):
                return player
            else:
                return None
        if (command == "s"):
            player = Player(name, current_player.current_room.s_to)
            if (player.current_room != None):
                return player
            else:
                return None
        if (command == "e"):
            player = Player(name, current_player.current_room.e_to)
            if (player.current_room != None):
                return player
            else:
                return None
        if (command == "w"):
            player = Player(name, current_player.current_room.w_to)
            if (player.current_room != None):
                return player
            else:
                return None


if __name__ == "__main__":
    name = input("Input your name: ")
    player = Player(name, room["outside"])
    print(f"\nWelcome to your adventure {player.name} \n")
    print("------------------------------ \n")
    while True:
        print(f"You are currently in {player.current_room.name} \n")
        print(f"{player.current_room.description} \n")
        print("------------------------------ \n")
        command = input("Enter a command, enter 'help' for details: ")

        if any(x in command for x in ['n', 's', 'e', 'w', 'search', 'look', 'pickup', 'get', 'inventory', 'drop', 'help', 'q']):
            if (command == "q"):
                exit()
            if (command == "help"):
                print("\n Move with [n, s, e, w] \n Look around for items with 'search' and 'look' \n Pick up and drop items with 'pickup / get' and 'drop' \n Open your inventory with 'inventory' \n Enter 'q' to quit the game ")

            print("------------------------------ \n")

            if command in ['search', 'look']:
                print(f"The following item/s are in this room \n")
                for x in (player.current_room.items):
                    print("name:", x.name, " | description:", x.description, " \n")

            if any(s in command for s in ("pickup", "get")):
                item = command.split()
                if(len(item) > 1):
                    item_name = (item[1]).capitalize()
                    selected_item = [x for x in player.current_room.items if x.name == item_name]
                    if (len(selected_item) >= 1):
                        player.getItem(selected_item)
                        for x in range(len(player.current_room.items)):
                            if ((player.current_room.items[x-1].name) == selected_item[0].name):
                                player.current_room.items.pop(x-1)
                        print(f"You've picked up the {selected_item[0].name} \n")
                    else:
                        print("That item does not exist \n")
                else:
                    print("Please specify which item to pickup \n")

            if (command == "inventory"):
                if ((len(player.items) > 0)):
                    print("The following item/s is in your inventory \n")
                    for x in player.items:
                        print("name:", x[0].name, " | description:", x[0].description, " \n")
                else:
                    print("You do not have any item in your inventory \n")

            if any(x in command for x in ("drop", "remove")):
                to_drop = command.split()
                if(len(to_drop) > 1):
                    toDropFormated = (to_drop[1]).capitalize()
                    dropped_item = [x for x in player.items if x[0].name == toDropFormated]
                    if (len(dropped_item) > 0):
                        dropped_formated = dropped_item[0][0]
                        player.dropItem(dropped_formated)
                    else:
                        print("That item is not in your inventory \n")
                else:
                    print("Please specify which item to drop \n")

            if command in ['n', 's', 'e', 'w']:
                holder = move(command, name, player)
                if (holder != None):
                    player = holder
                else:
                    print("You can't go that way \n")
        else:
            print("\nInvalid action \n")