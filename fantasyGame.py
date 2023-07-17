#!/usr/bin/env python
"""This is a Dnd-esque text-based game. The player is an adventurer in a standard fantasy medieval world and their end goal is to defeat
the evil king. In order to do so, they have to earn a fancy weapon by having enough xp. Xp is gained by winnning fights. Fights deplete 
the player's hp, which has to be replenished by eating or drinking health potions. Food and potions are purchased at the market. Money 
and other valuables can be obtained by going on adventures. The player can talk to NPC's, who may offer information and tips, or just
idle commentary on the area around them. Some NPC's may react differently to the player depending on their race/class, which are 
chosen by the player at the beginning of the game. If the player's hp ever goes down to 0, the player dies and restarts the game."""

import random
import yaml
import click

# classes/functions etc
class Item:
    """creates an item for the market"""

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}@{self.price}"

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.name == other.name
        else:
            return False
    
    def __hash__(self):
        return hash(self.name)


class Player:
    """why do i need to do this"""
    inventory: dict
    state_attrs = ["race", "pclass", "gold_coins"]

    def __init__(self, name: str = "", inventory: dict = {}):

        self.race = ""
        self.pclass = ""
        self.hp = 25
        self.xp = 0
        self.gold_coins = 50

        if name:
            self.name = name
        else:
            self.name = input("What is your name? ")
            # choosing race
            race = ""
            print(
                f"What is your race {self.name}?\n 1. Human\n 2. Orc\n 3. Dwarf\n 4. Elf\n 5. Halfling\n 6. Dragonborn\n 7. Gnome"
            )
            race = input("Please choose by entering a number between 1 and 7: ")

            while self.race == "":
                if race == "1":
                    self.race = "Human"
                elif race == "2":
                    self.race = "Orc"
                elif race == "3":
                    self.race = "Dwarf"
                elif race == "4":
                    self.race = "Elf"
                elif race == "5":
                    self.race = "Halfling"
                elif race == "6":
                    self.race = "Dragonborn"
                elif race == "7":
                    self.race = "Gnome"
                else:
                    print("Answer invalid, please try again.")
                    print(
                        "What is your race?\n 1. Human\n 2. Orc\n 3. Dwarf\n 4. Elf\n 5. Halfling\n 6. Dragonborn\n 7. Gnome"
                    )
                    race = input("Please choose by entering a number between 1 and 7: ")

            class_choice = ""
            print(
                "What is your class?\n 1. Barbarian\n 2. Bard\n 3. Cleric\n 4. Druid\n 5. Rogue\n 6. Ranger\n 7. Sorcerer\n 8. Monk"
            )
            class_choice = input("Please choose by entering a number between 1 and 8: ")

            while self.pclass == "":
                if class_choice == "1":
                    self.pclass = "Barbarian"
                elif class_choice == "2":
                    self.pclass = "Bard"
                elif class_choice == "3":
                    self.pclass = "Cleric"
                elif class_choice == "4":
                    self.pclass = "Druid"
                elif class_choice == "5":
                    self.pclass = "Rogue"
                elif class_choice == "6":
                    self.pclass = "Ranger"
                elif class_choice == "7":
                    self.pclass = "Sorcerer"
                elif class_choice == "8":
                    self.pclass = "Monk"
                else:
                    print("Answer invalid, please try again.")
                    print(
                        "What is your class?\n 1. Barbarian\n 2. Bard\n 3. Cleric\n 4. Druid\n 5. Rogue\n 6. Ranger\n 7. Sorcerer\n 8. Monk"
                    )
                    class_choice = input(
                        "Please choose by entering a number between 1 and 8: "
                    )


        if inventory:
            self.inventory = inventory
        else:
            self.inventory = {
                Item("feet of rope", 5): 50,
                Item("health potion", 5): 1,
                Item("sword", 5): 1,
                Item("bedroll", 5): 1,
                Item("leather armor", 5): 1,
                Item("ration packs", 5): 10,
                Item("dagger", 5): 2,
                Item("tent", 5): 1,
            }


    def update_inventory(self, item: Item, quantity: int):
        """updates your inventory. for the third time, duh"""
        self.inventory[item] = self.inventory.get(item, 0) + quantity
        return self

    def print_inv(self):
        """prints your inventory. duh"""
        print(f"{self.name}'s Inventory:")
        for item, quantity in self.inventory.items():
            print(f"\t{quantity:d} {item.name}")

    def see_stats(self):
        """lets you see your stats. again, duh"""
        print(f"Hello, {self.name}. Here are your statistics!")
        print(
            f"Race: {self.race}\nClass: {self.pclass}\nHit points: {self.hp}\nXP: {self.xp}\nGold Coins: {self.gold_coins}"
        )
        self.print_inv()
    
    def load(self, name, state, item_index):
        for v in self.state_attrs:
            state[v] = setattr(self, v, state.get(v, None))
        
        inventory = state.get("inventory", {})

        self.inventory = {
            item_index[ name ] : count
            for name, count in inventory.items()
        }

        return self

    def get_state(self):
        state = {}
        for v in self.state_attrs:
            state[v] = getattr(self, v)

        state["inventory"] = {
            item.name: count
            for item, count in self.inventory.items()
        }

        return state

class NotEnoughItems(Exception):
    """Tells the player there were not enough items"""
    pass

class NotEnoughMoney(Exception):
    """Tells the player they don't have enough money"""
    pass

def check_amt_items(item: Item, quantity: int, max_budget: int) -> int:
    while True:
        print(f"There are {quantity} {item.name} available for purchase. Each {item.name} costs {item.price}.")
        
        try:
            num_bought = int(input("How many would you like to buy? "))
            if num_bought > quantity:
                raise NotEnoughItems(f"Sorry, we don't have that many {item.name}. Please try again.")
            elif num_bought * item.price > max_budget:
                raise NotEnoughMoney(f"Sorry, that would cost {num_bought * item.price}, you only have {max_budget}")
        except TypeError:
            print("Sorry, invalid answer. Please try again.")
        except (NotEnoughItems, NotEnoughMoney) as error:
            print(str(error))
        except Exception as err:
            print(f"Not sure what's going on ... {err}")
        else:
            if num_bought == 0:
                print("Thank you for looking at our wares. Have a good day!")
            else:
                print("Thank you for your purchase, have a good day!")

            return num_bought

def buy_item(seller: Player, customer: Player, item: Item) -> Player:
    """Lets the player buy something"""

    num_bought = check_amt_items(item, seller.inventory[item], customer.gold_coins)
    
    if num_bought > 0:
        cost = num_bought * item.price
        print(f"Okay, that will be {cost} for {num_bought} of {item.name}. Here you go!")
        
        customer.gold_coins -= cost
        customer.update_inventory(item, num_bought)

        seller.update_inventory(item, -num_bought)
        seller.gold_coins += cost

    return seller

def choose_market_items(seller, customer, item_index):
    """
    Go through choices for seller to sell"""

    while True:
        print("Here is my current inventory")
        seller.print_inv()

        item_name = input("What would you like to buy? ")
        item = item_index[item_name]
        
        if item in seller.inventory:
            buy_item(seller, customer, item)
            return True

def choose_activities(config, config_path, player, market, item_index):
    """lets the player choose between checking their inventory, raiding a dragon hoard, exploring a dungeon, going monster hunting, going to town, or leaving the game"""
    while True:

        config["state"]["market"] = market.get_state()
        config["players"][player.name] = player.get_state()
        _state = yaml.dump( config )

        with open(config_path, "wt") as handle:
            handle.write(_state)

        print("")
        print(
            "\n ".join([
                f"What would you like to do, {player.name}?",
                "1. Check inventory",
                "2. Raid dragon hoard",
                "3. Explore dungeon",
                "4. Go monster hunting",
                "5. Go to town",
                "6. Buy something at the market",
                "7. Show market inventory",
                "8. Quit game"
            ])
        )
        choice = input("\nPlease enter your choice: ")

        if choice == "1":
            player.print_inv()
        elif choice == "2":
            # raid dragon hoard
            print("ELEPHANT, raided dragon hoard")
        elif choice == "3":
            # explore dungeon
            print("ELEPHANT, explored dungeon")
        elif choice == "4":
            # go monster hunting
            print("ELEPHANT, hunted monsters")
        elif choice == "5":
            # go to town
            print("ELEPHANT, went to town")
        elif choice == "6":
            choose_market_items(market, player, item_index)
        elif choice == "7":
            market.print_inv()
        elif choice == "8":
            print(f"Sorry to see you go, {player.name}. Until next time!")
            view_stats = input("Would you like to see your stats? Y/N ")

            while view_stats.lower() != "y" or "n":
                if view_stats.lower() == "y":
                    player.see_stats()
                    break
                elif view_stats.lower() == "n":
                    print("Okay, thank you for playing!")
                    break
                else:
                    print("Sorry, I didn't quite catch that.")
                    view_stats = input("Would you like to see your stats? Y/N ")

            exit()
        else:
            print("Answer invalid, please try again.")
            print(
                "What would you like to do? \n 1. Check inventory\n 2. Raid dragon hoard\n 3. Explore dungeon\n 4. Go monster hunting\n 5. Go to town\n 6. Quit game"
            )
            choice = input("Please enter your choice: ")

@click.command()
@click.argument("config_path")
def run(config_path):
    
    with open(config_path, "rt") as f:
        config = yaml.safe_load(f)
    
    items = set()
    for name,cost in config.get("items", {}).items():
        items.add( Item(name, cost) )
    
    item_index = {
        item.name : item
        for item in items
    }
    # opening screen - player chooses name, race, and class

    print("Welcome to the fantasy game!")
    
    players = sorted({ name for name in config["players"].keys() if name != "defaults" })

    player = None

    if players:
        print("Current players")
        for name in players:
            print(f"\t{name}")

        chosen_player = input("Who do you want to play as? ")
        if chosen_player in players:
            player = Player( name = chosen_player )
            player.load(chosen_player, 
                        config["players"][chosen_player],
                        item_index)
        else:
            print(f"{chosen_player} doesn't exist, lets make a new one")
    
    if not player:
        player = Player( inventory= {
                        item_index[name]: count
                        for name,count in config["players"]["defaults"]["inventory"].items()
                    })
    
    market = Player(name ="Market", inventory = {})
    market.load("Market", config["state"]["market"], item_index)

    # Raid dragon hoard

    # Explore dungeon

    # Go monster hunting

    # Go to town

    # choosing activities - player can check inventory, raid dragon hoard, explore dungeon, go monster hunting, or go to town
    choose_activities(config, config_path, player, market, item_index)

if __name__ == "__main__":
    run()