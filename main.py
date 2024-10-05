from room import Room
from character import Enemy, Character, Friend
from item import Item

# Room and character setup
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

# Create Enemy
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Hi, I'm Dave and I totally won't eat your brain.")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

# Create a friendly character
john = Character("John", "A friendly old man who knows the secrets of the mansion.")
john.set_conversation("Hello there! Can I help you?")
ballroom.set_character(john)

# Create a friendly character (Friend)
susan = Friend("Susan", "A kind woman who loves plants.")
susan.set_conversation("Hi there! Have you seen any flowers lately?")
susan.set_favorite_gift("flower")
kitchen.set_character(susan)

# Set room descriptions
kitchen.set_description("A dank and dirty room buzzing with flies.")
ballroom.set_description("A vast room with a shiny wooden floor.")
dining_hall.set_description("A large room with ornate golden decorations.")

# Link rooms and lock the ballroom
# Link rooms and lock the ballroom
kitchen.link_room(dining_hall, "south")  # Linking kitchen to dining hall to the south
dining_hall.link_room(kitchen, "north")  # Linking dining hall back to kitchen to the north
dining_hall.link_room(ballroom, "west", locked=True)  # Linking dining hall to ballroom to the west (locked)
ballroom.link_room(dining_hall, "east")  # Linking ballroom back to dining hall to the east



# Create a Key item
key = Item("key", "A small rusty key.")
dining_hall.set_item(key)  # Place the key in the dining hall

current_room = kitchen
inventory = []  # Player's inventory to store items

# Main game loop
while True:
    print("\n")
    current_room.get_details()

    # Check for characters in the room
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    # Check for items in the room
    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ").strip().lower()  # Normalize command input

    if command in ["north", "south", "east", "west"]:
        if command == "west" and current_room.linked_rooms[command].is_locked:
            if key in inventory:  # Check if the player has the key
                print(f"You use the {key.get_name()} to unlock the door.")
                current_room.linked_rooms[command].is_locked = False  # Unlock the room
                current_room = current_room.move(command)  # Now move into the room
            else:
                print("The door is locked. You need a key to enter.")
        else:
            current_room = current_room.move(command)  # Move normally if not locked
    elif command == "take":
        if item is not None:
            print(f"You take the {item.get_name()}.")
            inventory.append(item)  # Store the actual item object, not just the name
            current_room.set_item(None)  # Remove the item from the room
        else:
            print("There's nothing to take.")
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There's no one here to talk to.")
    elif command == "hug":
        if isinstance(inhabitant, Friend):
            inhabitant.hug()
        else:
            print("You can't hug this character.")
    elif command == "gift":
        if isinstance(inhabitant, Friend):
            gift = input("Enter gift: ")
            inhabitant.give_gift(gift)
        else:
            print("This character doesn't seem interested in gifts.")
    elif command == "fight":
        if isinstance(inhabitant, Enemy):
            item_name = input("Enter item here: ")
            if inhabitant.fight(item_name):
                current_room.set_character(None)
            else:
                print("You lost the fight. Game over.")
                break
        else:
            print("There's no one here to fight.")
    elif command == "bribe":
        if isinstance(inhabitant, Enemy):
            amount = int(input("Enter bribe amount: "))
            if inhabitant.bribe(amount):
                current_room.set_character(None)
            else:
                print("Bribe failed.")
        else:
            print("You can't bribe this person.")
    elif command == "steal":
        if isinstance(inhabitant, Enemy):
            inhabitant.steal()
        else:
            print("You can't steal from this person.")
    elif command == "sleep":
        if isinstance(inhabitant, Enemy):
            if inhabitant.put_to_sleep():
                current_room.set_character(None)
        else:
            print("You can't put this person to sleep.")
    else:
        print("Invalid command.")

