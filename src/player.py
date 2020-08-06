# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def getItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        for x in range(len(self.items)):
            if ((self.items[x-1][0].name) == item.name):
                self.items.pop(x-1)
                print(f"You've dropped the {item.name} \n")