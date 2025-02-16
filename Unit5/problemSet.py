class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    def set_catchphrase(self, new_catchphrase):
    
        if len(new_catchphrase) < 20 and any(c.isalpha() for c in new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase Updated!")
        else:
            print("Invalid catchphrase")

    def add_item(self, item_name):
        listOfItems = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu","cacao tree"]

        if item_name in listOfItems:
            self.furniture.append(item_name)

    def print_inventory(self):
        from collections import Counter
        if len(self.furniture) == 0:
            print("Inventory Empty!")
            return

        freqOfItems = Counter(self.furniture)
        for item, quantity in freqOfItems.items():
            print(f"{item}: {quantity}, ", end="")
            

def of_personality_type(townies, personality_type):
    result = []
    for villager in townies:
        if villager.personality == personality_type:
            result.append(villager.name)
    return result

def message_received(start_villager, target_villager):

    while start_villager.neighbor != None:
        if start_villager.neighbor.name == target_villager.name:
            return True
        start_villager = start_villager.neighbor
    if start_villager == target_villager.name:
        return True
    else:
        return False

            
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

"""
Using the linked list from Problem 9, create a new Node timmy with value "Timmy" 
and place it between tom_nook and tommy so the new linked list is tom_nook -> timmy -> tommy.
"""

timmy = Node("Timmy")
tom_nook = Node("Tom Nook")
tommy = Node("Tommy") 
tom_nook.next = tommy


prev = tom_nook.next
tom_nook.next = timmy
timmy.next = prev


saharah = Node("Saharah")
tommy.next = saharah
tom_nook.next = None


def print_list(head):
    curr = head
    while curr.next != None:
        print(f"{curr.value} -> ", end="")
        curr = curr.next
    print(f"{curr.value}")

isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj

print_list(isabelle)
