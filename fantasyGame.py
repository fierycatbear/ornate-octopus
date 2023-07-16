#!/usr/bin/env python

"""This is a Dnd-esque text-based game. The player is an adventurer in a standard fantasy medieval world and their end goal is to defeat
the evil king. In order to do so, they have to earn a fancy weapon by having enough xp. Xp is gained by winnning fights. Fights deplete 
the player's hp, which has to be replenished by eating or drinking health potions. Food and potions are purchased at the market. Money 
and other valuables can be obtained by going on adventures. The player can talk to NPC's, who may offer information and tips, or just
idle commentary on the area around them. Some NPC's may react differently to the player depending on their race/class, which are 
chosen by the player at the beginning of the game. If the player's hp ever goes down to 0, the player dies and restarts the game."""

#classes/functions etc
class Item:
    
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class Player:

    def __init__(self):

        self.name = input("What is your name? ")
        self.race = ""
        self.pclass = ""
        self.hp = 25
        self.xp = 0
        self.gold_coins = 50
        self.inventory = {'feet of rope': 50, 'health potion': 1, 'sword': 1, 'bedroll': 1, 'leather armor': 1, 'ration packs': 10, 'dagger': 2, 'tent':1 }

        #choosing race
        race = ""
        print("What is your race?\n 1. Human\n 2. Orc\n 3. Dwarf\n 4. Elf\n 5. Halfling\n 6. Dragonborn\n 7. Gnome")
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
                print("What is your race?\n 1. Human\n 2. Orc\n 3. Dwarf\n 4. Elf\n 5. Halfling\n 6. Dragonborn\n 7. Gnome")
                race = input("Please choose by entering a number between 1 and 7: ")
        
        class_choice = ""
        print("What is your class?\n 1. Barbarian\n 2. Bard\n 3. Cleric\n 4. Druid\n 5. Rogue\n 6. Ranger\n 7. Sorcerer\n 8. Monk")
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
                print("What is your class?\n 1. Barbarian\n 2. Bard\n 3. Cleric\n 4. Druid\n 5. Rogue\n 6. Ranger\n 7. Sorcerer\n 8. Monk")
                class_choice = input("Please choose by entering a number between 1 and 8: ")

def print_inv():
    print(f"{p1.name}'s Inventory:")
    for k,v in p1.inventory.items():
        print(v, k)   

def see_stats():
    print(f"Hello, {p1.name}. Here are your statistics!")
    print(f"Race: {p1.race}\nClass: {p1.pclass}\nHit points: {p1.hp}\nXP: {p1.xp}\nGold Coins: {p1.gold_coins}")
    print_inv()
"""
def check_amt_items(item):
    while True:
        print(f"There are {item.quantity} {item.name} available for purchase. Each {item.name} costs {item.price}.")
        num_bought = int(input("How many would you like to buy?"))

        while num_bought != int:
            print("Sorry, invalid answer. Please try again.")
            print(f"There are {item.quantity} {item.name} available for purchase. Each {item.name} costs {item.price}.")
            num_bought = int(input("How many would you like to buy?"))

        while num_bought > item.quantity:
            print(f"Sorry, we don't have that many {item.name}. Please try again.")
            print(f"There are {item.quantity} {item.name} available for purchase. Each {item.name} costs {item.price}.")
            num_bought = int(input("How many would you like to buy?"))

        while num_bought == 0:
            print("Thank you for looking at our wares. Have a good day!")
            exit()
        
        break

def buy_item(item):
    num_bought = 0
    cost = 0

    #check if player can buy that amount of items
    check_amt_items(item)

    #check if player can afford the items
    while True:
        cost = num_bought*item.price

        while cost > p1.gold_coins:
            print("Sorry, you don't have enough gold for this transaction. Please try a smaller quantity, or type 0 to leave this booth.")
            check_amt_items(item)
            cost = num_bought*item.price
        
        if cost <= p1.gold_coins:
            print(f"Okay, that will be {cost} for {num_bought} of {item.name}. Here you go!")
            p1.gold_coins -= cost
            update_inventory(item, num_bought)
"""
def update_inventory(item, quantity):
    if item not in dict:
        p1.inventory.update({item: quantity})
    else:
        p1.inventory[item] = quantity


def choose_activities():
    while True:
        print("What would you like to do? \n 1. Check inventory\n 2. Raid dragon hoard\n 3. Explore dungeon\n 4. Go monster hunting\n 5. Go to town\n 6. Quit game")
        choice = input("Please enter your choice: ")

        if choice == "1":
            print_inv()
        elif choice == "2":
            #raid dragon hoard
            print("ELEPHANT, raided dragon hoard")
        elif choice == "3":
            #explore dungeon
            print("ELEPHANT, explored dungeon")
        elif choice == "4":
            #go monster hunting
            print ("ELEPHANT, hunted monsters")
        elif choice == "5":
            #go to town
            print("ELEPHANT, went to town")
            buy_item(carrot)
        elif choice == "6":
            print(f"Sorry to see you go, {p1.name}. Until next time!")
            viewStats = input("Would you like to see your stats? Y/N ")
            
            while viewStats.lower() != "y" or "n":
                if viewStats.lower() == "y":
                    see_stats()
                    break
                elif viewStats.lower() == "n":
                    print("Okay, thank you for playing!")
                    break
                else:
                    print("Sorry, I didn't quite catch that.")
                    viewStats = input("Would you like to see your stats? Y/N ")

            quit()
        else:
            print("Answer invalid, please try again.")
            print("What would you like to do? \n 1. Check inventory\n 2. Raid dragon hoard\n 3. Explore dungeon\n 4. Go monster hunting\n 5. Go to town\n 6. Quit game")
            choice = input("Please enter your choice: ")

#opening screen - player chooses name, race, and class 

print ("Welcome to the fantasy game!")    
p1 = Player()


#Raid dragon hoard

#Explore dungeon

#Go monster hunting

#Go to town

#choosing activities - player can check inventory, raid dragon hoard, explore dungeon, go monster hunting, or go to town
update_inventory("chicken nuggets", 12)
update_inventory("sword", 2)
choose_activities()