from character import Character, Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.describe()

dave.set_conversation("Hi Im Dave and totally wont eat your brain")
dave.talk()
dave.set_weakness("cheese")
print("What will you fight with?")
fight_with = input("Enter item here:")
dave.fight(fight_with)
# Create a friendly character
john = Character("John", "A friendly old man who knows the secrets of the mansion.")
john.set_conversation("Hello there! Can I help you?")

