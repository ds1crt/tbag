class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(f"{self.name} is in this room!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name}] says: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk with you.")
    
    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight with you.")
        return True
    
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness
    
    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item.lower() == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False
        
    def bribe(self, amount):
        if amount >= 50:  # Example threshold
            print(f"{self.name} accepts the bribe and lets you pass.")
            return True
        else:
            print(f"{self.name} is insulted by your low offer and attacks!")
            return False

    def steal(self):
        print(f"You try to steal from {self.name}. They are too quick!")
        return False
    
    def put_to_sleep(self):
        print(f"You use a sleeping spell on {self.name}. They fall asleep.")
        return True

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.favorite_gift = None
    
    def set_favorite_gift(self, gift):
        self.favorite_gift = gift

    def hug(self):
        print(f"{self.name} gives you a big, warm hug! You feel comforted.")
    
    def give_gift(self, gift):
        if gift == self.favorite_gift:
            print(f"{self.name} smiles and says, 'Thank you for the {gift}! You know me so well.'")
        else:
            print(f"{self.name} says, 'Thanks... but {gift} isn't really my favorite.'")

