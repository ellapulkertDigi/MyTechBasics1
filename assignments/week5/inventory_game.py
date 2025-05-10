
# --- Game State --
MAX_BOUQUET_SIZE = 5           # How many flowers/fillers can fit in the bouquet

inventory = []                 # Everything the player carries (bouquet + tools)

rooms = {                      # All locations in the shop, keyed by name
    "shop_entrance": {
        "description": "You stand in the entrance. The scent of fresh flowers fills the air.",
        "items": [
            {"name": "Rose",        "type": "flower",   "description": "A classic red rose."},
            {"name": "Tulip",       "type": "flower",   "description": "A bright yellow tulip."},
            {"name": "Scissors",    "type": "tool",     "description": "For trimming stems."}
        ],
        "exits": {"north": "cool_room"}
    },

    "cool_room": {
        "locked": True,   # becomes False after using the Scissors once
        "description": "The refrigerated room keeps exotic flowers fresh.",
        "items": [
            {"name": "Orchid",       "type": "flower",   "description": "A delicate orchid."},
            {"name": "Baby's Breath","type": "filler",   "description": "Tiny white cloud-like flowers."},
            {"name": "Lily",         "type": "flower",   "description": "A fragrant white lily."},
            {"name": "Carnation",    "type": "flower",   "description": "A pink carnation."}
        ],
        "exits": {"south": "shop_entrance", "east": "wrapping_station"}
    },

    "wrapping_station": {
        "description": "Here you can wrap and decorate your bouquet.",
        "items": [
            {"name": "Ribbon",   "type": "wrapping", "description": "A silky ribbon."},
            {"name": "Paper",    "type": "wrapping", "description": "Floral wrapping paper."},
            {"name": "Sunflower", "type": "flower", "description": "A tall, sun-loving bloom."},
        ],
        "exits": {"west": "cool_room"}
    }
}

current_room = "shop_entrance"


# ------------------------  Functions  -------------------------

def bouquet_items():
    """Return only the flowers and fillers inside the inventory."""
    return [item for item in inventory if item["type"] in ("flower", "filler")]


def find_item_in_room(item_name):
    """Return the dict of an item lying in the current room or None."""
    name_lc = item_name.lower()
    for itm in rooms[current_room]["items"]:
        if itm["name"].lower() == name_lc:
            return itm
    return None


def have_item(item_name):
    """True if the player already carries an item with that name (any type)."""
    name_lc = item_name.lower()
    return any(itm["name"].lower() == name_lc for itm in inventory)


# -----------------------  Core Player Actions  -----------------------

def show_inventory():
    if not inventory:
        print("You are not carrying anything.")
        return

    print("You are carrying:")
    for itm in inventory:
        print(f"  • {itm['name']} ({itm['type']})")


def show_room_items():
    room = rooms[current_room]
    print(room["description"])

    if room["items"]:
        print("Items here:")
        for itm in room["items"]:
            print(f"  • {itm['name']} ({itm['type']})")
    else:
        print("No loose items here.")

    # Show exits even if locked
    print("Exits:", ", ".join(room["exits"].keys()))


def examine(item_name):
    item_name_lc = item_name.lower()

    # Try inventory first
    for itm in inventory:
        if itm["name"].lower() == item_name_lc:
            print(f"{itm['name']}: {itm['description']}")
            return

    itm = find_item_in_room(item_name)
    if itm:
        print(f"{itm['name']}: {itm['description']}")
    else:
        print("You don't see that here.")


def drop(item_name):
    item_name_lc = item_name.lower()
    for itm in inventory:
        if itm["name"].lower() == item_name_lc:
            inventory.remove(itm)
            rooms[current_room]["items"].append(itm)
            if itm["type"] in ("tool", "wrapping"):
                print(f"You put down the {itm['name']}.")
            else:
                print(f"You remove {itm['name']} from your bouquet.")
            return
    print("You don't have that.")


def pick_up(item_name):
    name_lc = item_name.lower()
    room_items = rooms[current_room]["items"]

    # 1) Is the item lying here?
    for itm in room_items:
        if itm["name"].lower() == name_lc:

            # Flowers/fillers: enforce bouquet limit
            if itm["type"] in ("flower", "filler") and len(bouquet_items()) >= MAX_BOUQUET_SIZE:
                print("Your bouquet is full – drop a flower or filler first.")
                return

            room_items.remove(itm)
            inventory.append(itm)

            if itm["type"] in ("tool", "wrapping"):
                print(f"You pick up {itm['name']} and hold it at the ready.")
            else:
                print(f"You add {itm['name']} to your bouquet.")
            return

    # 2) Item not in room – clarify why
    if have_item(item_name):
        print(f"You already have {item_name}.")
    elif len(bouquet_items()) >= MAX_BOUQUET_SIZE:
        print("Your bouquet is already full – drop a flower or filler before adding more.")
    else:
        print("No such item here.")


def go(direction):
    global current_room
    dir_lc = direction.lower()
    room = rooms[current_room]

    if dir_lc not in room["exits"]:
        print("Can't go that way.")
        return

    target_key = room["exits"][dir_lc]
    target_room = rooms[target_key]

    # Locked cool room?
    if target_room.get("locked"):
        if have_item("Scissors"):
            target_room["locked"] = False
            print("You jimmy open the safety latch with the Scissors – the cool-room door clicks open!")
        else:
            print("The door is locked; maybe a tool could help.")
            return


    current_room = target_key
    show_room_items()


def use(item_name):
    item_name_lc = item_name.lower()

    # Must be carrying the item:
    for itm in inventory:
        if itm["name"].lower() == item_name_lc:

            # ------------------  TOOL  ------------------
            if itm["type"] == "tool" and itm["name"].lower() == "scissors":
                print("You trim a few stems – everything looks neat.")
                return

            # ----------------  WRAPPING  ----------------
            if itm["type"] == "wrapping":
                if not bouquet_items():
                    print("You need at least one flower to wrap!")
                    return
                rating = evaluate_bouquet()        # <-- see helper below
                print(f"You wrap your bouquet neatly with the {itm['name']}.")
                print(rating)
                print("You win! 🌺")
                exit()


            print("That item can't be 'used' directly.")
            return

    print("You don't have that.")


# ------------  End-game Bouquet Rating Helper  -----------------

def evaluate_bouquet():
    exotic_names = {"Orchid", "Lily"}   # treat these as exotic
    exotics = [f for f in bouquet_items() if f["name"] in exotic_names]

    if len(exotics) >= 3:
        return "The bouquet looks luxurious and exotic – perfect for a grand occasion."
    elif len(exotics) >= 1:
        return "A balanced bouquet with a hint of the exotic. Very tasteful!"
    else:
        return "A classic, down-to-earth bouquet that will please anyone."


# ----------------------------  Game Loop  ----------------------------

def game_loop():
    print("Welcome to the Flower-Shop Bouquet Builder! You can walk around and arrange a beautiful bouquet.")
    print("Type 'help' for a list of commands.")
    show_room_items()           # Give initial context

    while True:
        command = input("\n> ").strip().lower()

        if command == "help":
            print("Commands:")
            print("  inventory               – list what you're carrying")
            print("  look                    – look around the room again")
            print("  go <direction>          – move north / south / east / west")
            print("  pickup <item>           – pick something up")
            print("  drop <item>             – put something down")
            print("  use <item>              – use a tool or wrapping")
            print("  examine <item>          – read the item's description")
            print("  quit                    – exit the game")

        elif command == "inventory":
            show_inventory()

        elif command == "look":
            show_room_items()

        elif command.startswith("go "):
            go(command[3:])

        elif command.startswith("pickup "):
            pick_up(command[7:])

        elif command.startswith("drop "):
            drop(command[5:])

        elif command.startswith("use "):
            use(command[4:])

        elif command.startswith("examine "):
            examine(command[8:])

        elif command == "quit":
            print("Thanks for playing!")
            break

        else:
            print("Unknown command. Type 'help' for assistance.")


if __name__ == "__main__":
    game_loop()
