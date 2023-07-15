"""I am a module called inventory.
"""
import json

class BagTooHeavyError(Exception):
    """Simple exception to let you know the bag is too heavy"""
    pass

class Item:
    """This is the Item baseclass for all items"""
    def __init__(self, weight):
        self.weight = weight

    def serialize(self):
        """Serialize creates a json string of this item"""
        return json.dumps({
            "weight": self.weight
        })

class Rock(Item):
    pass 

class Bag(Item):
    """I'm a docstring"""

    def __init__(self, weight: float, capacity: float):
        super().__init__(weight)
        self.capacity = capacity
        self.current_load = 0.0
        self.contents = []

    def serialize(self):
        """Serialize creates a json string of this item"""
        return json.dumps({
            "weight": self.weight,
            "capacity": self.capacity
        })


    def can_hold(self, other_item: Item) -> bool:
        """Simple test if this bag can hold another item"""
        return (other_item.weight + self.current_load) <= self.capacity

    def add_item(self, other_item: Item):
        """Adds a single item to this Bag"""
        if self.can_hold(other_item):
            self.contents.append(other_item)
            self.current_load += other_item.weight
        else:
            raise BagTooHeavyError(f"Max capacity is {self.capacity}")

class BagOfHolding(Bag):
    def __init__(self, weight: float):
        super().__init__(weight, float("inf"))

bag_one = Bag(1.0, 3.0)
boh_one = BagOfHolding(2.0)
boh_two = BagOfHolding(2.0)

rock = Rock(1)

print( isinstance(boh_one, Item) )

try:
    print( bag_one.serialize() )
    print( boh_one.serialize() )

    boh_one.add_item(rock)
    bag_one.add_item(rock)
    print(bag_one.contents)
    bag_one.add_item(rock)
    print(bag_one.contents)
    bag_one.add_item(rock)
    print(bag_one.contents)
    bag_one.add_item(rock)
    print(bag_one.contents)

except TypeError as err:
    print("AAHHAHAHAHA")
except BagTooHeavyError as yourmom:
    print(f"That's too heavy for this bag: {yourmom}")
else:
    print("OOOHOHO")