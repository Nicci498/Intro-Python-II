from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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


player = Player(input("Who are you? "), room["outside"])

# Write a loop that:
print(f'Welcome! {player.name}. In order to navigate this strange new world, use n to move north, e to move east, s to move south, and of course w to move west')

nah = "The footing is treacherous, find another path"
while True:
    cmd = input("Choose a path ~~> ")
    status = f'{player.name} is at {player.current_room.name}. {player.current_room.description}'
    if cmd == 'n':
        if player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to
            print(status)
        else:
            print(nah)
        #if player's current room has a room to north that exists enter new room
        #if not send error reply
        pass
    elif cmd == 'e':
        if player.current_room.e_to is not None:
            player.current_room = player.current_room.e_to
            print(status)
        else:
            print(nah)
        #if current room has room to east that exists enter new room and print details
        #if not send error reply
        pass
    elif cmd == 's':
        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to
            print(status)
        else:
            print(nah)
        #if current room has room to south that exists enter new room and print details
        #if not send error reply
        pass
    elif cmd == 'w':
        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w_to
            print(status)
        else:
            print(nah)
        #if current room has room to west that exists enter new room and print details
        #if not send error reply
        pass
    elif cmd == 'q':
        print(f'We will miss you, {player.name}')
        break
    else:
        print('I dont understand what you want, use n to move north, e to move east, s to move south, and of course w to move west')
    

# -my Greeting screen with player name input and directions
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


#
# Main
# REPL -read eval print loop
# print("\033[1;32;40m Bright Green  \n")
# https://ozzmaker.com/add-colour-to-text-in-python/
# Make a new player object that is currently in the 'outside' room.


