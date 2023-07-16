#!/usr/bin/env python

"""the player goes to a market and can buy stuff, as long as they have the money for it
money is measured in gold coins as inherent part of player, so $$ = p1.gold_coins
items for sale will be ration packs, rope, health potion, swords, armor, dagger, and more"""
class Item:
    
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


def check_amt_items(item):
    while True:
        print(f"There are {item.quantity} {item.name} available for purchase. Each {item.name} costs {item.price}.")
        num_bought = int(input("How many would you like to buy?"))

        while num_bought != int:
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

def update_inventory(item, quantity):
    if item not in dict:
        p1.inventory.update({item: quantity})
    else:
        p1.inventory[item] = quantity
#the general function to buy an item will check if a player can get that amount of items, if they can afford the items, and then add them to the player's inventory
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


carrot = Item("carrot", 9, 10)

buy_item(carrot)

       
            
                
        



        
