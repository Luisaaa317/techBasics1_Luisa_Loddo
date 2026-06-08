## dictionaries
inventory = []
items_in_room = [
    {"name": "Towel", "type": "Essential", "description": "You can sit on the towel or dry yourself.", "use-message": "You are now dry and sitting on the towel."},
    {"name": "Sunglasses", "type": "Protection", "description": "Provides shade for you eyes.", "use-message": "Your eyes are now protected from the sun."},
    {"name": "Hat", "type": "Protection", "description": "Provides shade for your head.", "use-message": "Your head is now protected from the sun."},
    {"name": "Sunscreen", "type": "Protection", "description": "Saves you from getting a sunburn.", "use-message": "Your skin is now protected from the sun."},
    {"name": "Bathing-suit", "type": "Clothes", "description": "Should be worn when going swimming.", "use-message": "You're ready to take a bath."},
    {"name": "Watermelon", "type": "Food", "description": "Food in case you get hungry.", "use-message": "You're energized and fed now."},
    {"name": "Water", "type": "Food", "description": "Water in case you get thirsty.", "use-message": "You're sufficiently hydrated now."},
    {"name": "Book", "type": "Activity", "description": "Something to keep you busy when alone.", "use-message": "You're entertained now."},
    {"name": "Card-game", "type": "Activity", "description": "Something to keep you busy with friends.", "use-message": "You and your friends are entertained now."},
    {"name": "Umbrella", "type": "Protection", "description": "Provides shade for your body.", "use-message": "You are now protected from the sun."},
    {"name": "Ball", "type": "Activity", "description": "Something to keep you busy with friends.", "use-message": "You and your friends are entertained now."},
]

MAX_INVENTORY_SIZE = 5

DEBUG = True  

LEADERBOARD_FILE = "leaderboard.txt"

import time

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

def save_record(name, time_used):
    timestamp = time.strftime("%H:%M:%S")  
    record = f"{name},{timestamp},{time_used}\n"

    try:
        with open(LEADERBOARD_FILE, "a") as file:
            file.write(record)
        print(f"Record saved: {name} - {time_used} seconds at {timestamp}")
    except Exception as e:
        print(f"Error saving record: {e}")

def load_leaderboard():
    records = []
    try:
        with open(LEADERBOARD_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 3:
                        name, timestamp, time_used = parts
                        records.append({
                            "name": name,
                            "timestamp": timestamp,
                            "time_used": int(time_used)
                        })
    except FileNotFoundError:
        print("No previous records found. Creating new file...")
        try:
            with open(LEADERBOARD_FILE, "w") as file:
                pass
        except Exception as e:
            print(f"Could not create file: {e}")
    except Exception as e:
        print(f"Error loading records: {e}")

    return records


def show_leaderboard():
    records = load_leaderboard()
    if not records:
        print("No records yet.")
        return

    print("\n--- Leaderboard ---")
    sorted_records = sorted(records, key=lambda x: x["time_used"])
    for i, record in enumerate(sorted_records, 1):
        print(f"{i}. {record['name']} - {record['time_used']} seconds - {record['timestamp']}")

def get_time_used(start_time):
    return int(time.time() - start_time)

# game loop
def game_loop():
    print("Welcome to the Beach Game!")
    print("You're at the beach but lost all your belongings on the way. Let's go retrieve them!")
    print("Type 'help' for a list of commands.")

    if DEBUG:
        print("\nDEBUG MODE: Skipping game...")
        name = input("Enter your name for testing: ").strip()
        if not name:
            name = "Player"
        save_record(name, 120)
        print("Test record saved. You can now play the game!")
    else:
        print("Starting the game...")

    start_time = time.time()

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
                name = input("Enter your name: ").strip()
                if not name:
                    name = "Player"
                time_used = get_time_used(start_time)
                save_record(name, time_used)
                show_leaderboard()
                print("Thanks for playing!")
                break
            case _:  
                print("Unknown command. Type 'help' to see available commands.")
# main function

if __name__ == "__main__":
    game_loop()
