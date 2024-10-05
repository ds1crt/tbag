class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.is_locked = False
        self.item = None  # Initialize item attribute

    def get_description(self):
        return self.description
    
    def set_description(self, room_description):
        self.description = room_description

    def describe(self):
        print(self.description)

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name
    
    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def link_room(self, room, direction, locked=False):
        self.linked_rooms[direction] = room
        room.is_locked = locked  # This should not lock the current room


    def set_item(self, item):  # Method to set an item in the room
        self.item = item

    def get_item(self):  # Method to retrieve the item in the room
        return self.item

    def get_details(self):
        """Displays the room details and linked rooms."""
        print(f"You are in the {self.name}")
        print("--------------------------------")
        print(self.description)
        for direction, room in self.linked_rooms.items():
            print(f"The {room.get_name()} is {direction}")

    def move(self, direction, key=None):
        if direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            if room.is_locked:
                if key is not None:  # Check if a key is provided
                    print(f"You use the {key.get_name()} to unlock the door.")
                    room.is_locked = False  # Unlock the room
                else:
                    print("The door is locked. You need a key to enter.")
                    return self  # Stay in the current room if locked
            return room  # Move to the linked room
        else:
            print("You can't go that way.")
            return self  # Stay in the current room if the direction is invalid
