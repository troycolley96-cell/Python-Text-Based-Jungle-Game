# Text-Based Adventure Game
# Serpent of the Forgotten Temple

def show_instructions():
    print("Serpent of the Forgotten Temple")
    print("You are a sentient python slithering through an ancient jungle temple.")
    print("Collect all 6 artifacts before entering the Panther’s Lair.")
    print("Commands:")
    print("  North, South, East, West")
    print("  get <item>")
    print("-" * 50)


rooms = {
    'Jungle Temple Entrance': {
        'East': 'Courtyard'
    },
    'Courtyard': {
        'West': 'Jungle Temple Entrance',
        'North': 'Vine-Covered Shrine',
        'South': 'Ancient Library',
        'East': 'Destroyed Campsite',
        'item': 'Sun Medallion'
    },
    'Vine-Covered Shrine': {
        'South': 'Courtyard',
        'East': 'Waterfall Chamber',
        'item': 'Ancient Idol'
    },
    'Waterfall Chamber': {
        'West': 'Vine-Covered Shrine',
        'item': 'Crystal Feather'
    },
    'Ancient Library': {
        'North': 'Courtyard',
        'East': 'Chimpanzee Pit',
        'item': 'Mysterious Scroll'
    },
    'Chimpanzee Pit': {
        'West': 'Ancient Library',
        'item': 'Tribal Necklace'
    },
    'Destroyed Campsite': {
        'West': 'Courtyard',
        'North': 'Panther’s Lair',
        'item': 'Cursed Tablet'
    },
    'Panther’s Lair': {
        'South': 'Destroyed Campsite'
    }
}

current_room = 'Jungle Temple Entrance'
inventory = []

show_instructions()

while True:
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {inventory}")

    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")

    command = input("Enter your move: ").strip().lower()
    command_words = command.split()

    # Movement
    if command.capitalize() in ['North', 'South', 'East', 'West']:
        direction = command.capitalize()

        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]

            # Villain check
            if current_room == 'Panther’s Lair':
                if len(inventory) < 6:
                    print("\nThe Jungle Guardian Panther lunges from the shadows!")
                    print("You were not prepared. Game Over.")
                    break
                else:
                    print("\nWith all artifacts united, the Panther retreats.")
                    print("You escape the Forgotten Temple. YOU WIN!")
                    break
        else:
            print("You cannot slither that way.")

    # Get item
    elif command_words[0] == 'get':
        item_name = " ".join(command_words[1:]).title()

        if 'item' in rooms[current_room] and item_name == rooms[current_room]['item']:
            inventory.append(item_name)
            print(f"{item_name} collected!")
            del rooms[current_room]['item']
        else:
            print("That item is not here.")

    else:
        print("Invalid command. Try North, South, East, West, or get <item>.")