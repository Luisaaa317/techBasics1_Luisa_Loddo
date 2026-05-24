# dictionaries 
inventory = []
items_in_room = [
    {"name": "Towel", "type": "Essential", "description": "You can sit on the towel or dry yourself.", "use-message": "You are now dry and sitting on the towel."},
    {"name": "Sunglasses", "type": "Protection", "description": "Provides shade for you eyes.", "use-message": "Your eyes are now protected from the sun."},
    {"name": "Hat", "type": "Protection", "description": "Provides shade for your head.", "use-message": "Your head is now protected from the sun."},
    {"name": "Sunscreen", "type": "Protection", "description": "Saves you from getting a sunburn.", "use-message": "Your skin is now protected from the sun."},
    {"name": "Bathing suit", "type": "Clothes", "description": "Should be worn when going swimming.", "use-message": "You're ready to take a bath."},
    {"name": "Watermelon", "type": "Food", "description": "Food in case you get hungry.", "use-message": "You're energized and fed now."},
    {"name": "Water", "type": "Food", "description": "Water in case you get thirsty.", "use-message": "You're sufficiently hydrated now."},
    {"name": "Book", "type": "Activity", "description": "Something to keep you busy when alone.", "use-message": "You're entertained now."},
    {"name": "Card game", "type": "Activity", "description": "Something to keep you busy with friends.", "use-message": "You and your friends are entertained now."},
    {"name": "Umbrella", "type": "Protection", "description": "Provides shade for your body.", "use-message": "You are now protected from the sun."},
    {"name": "Ball", "type": "Activity", "description": "Something to keep you busy with friends.", "use-message": "You and your friends are entertained now."},

] 
MAX_INVENTORY_SIZE = 5

# functions

def show_inventory():
    if inventory == []:
        print("You have no inventory.")
    else:
        print("These items are in your inventory:")
        for i in inventory:
            print(f"{i['name']}")

def show_room_items():
    print("These items are in the room:")
    for i in items_in_room:
        print(f"{i['name']}")


def pick_up(item_name):
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your inventory is full. Please use or drop an item before picking up a new one.")
        return False
    for item in items_in_room:
        if item["name"].lower() == item_name.lower():
            items_in_room.remove(item)
            inventory.append(item)
            print(f"You picked up: {item_name}")
            return True
    print(f"Item '{item_name}' not found in the room.")
    return False


def drop(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            inventory.remove(item)
            items_in_room.append(item)
            print(f"You dropped: {item_name}")
            return True
    print(f"You don't have '{item_name}' in your inventory.")
    return False


def use(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            inventory.remove(item)
            print(f"{item['use-message']}")
            return True
    print(f"You don't have '{item_name}' in your inventory.")
    return False


def examine(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            print(f"\n--- {item['name']} ---")
            print(f"Type: {item['type']}")
            print(f"Description: {item['description']}")
            return True

    for item in items_in_room:
        if item["name"].lower() == item_name.lower():
            print(f"\n--- {item['name']} ---")
            print(f"Type: {item['type']}")
            print(f"Description: {item['description']}")
            return True

    print("Item does not exist.")
    return False

# game loop

def game_loop():
    print("Welcome to the Beach Game!")
    print("You're at the beach but lost all your belongings on the way. Let's go retrieve them!")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()



        match command.split():
            case ["help"]:
                print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit")
            case ["inventory"]:
                show_inventory()
            case ["look"]:
                show_room_items()
            case ["pickup", item_name]:
                pick_up(item_name)
            case ["drop", item_name]:
                drop(item_name)
            case ["use", item_name]:
                use(item_name)
            case ["examine", item_name]:
                examine(item_name)
            case ["quit"]:
                print("Thanks for playing!")
                break
            case _: # else
                print("Unknown command. Type 'help' to see available commands.")

# main function

if __name__ == "__main__":
    game_loop()



