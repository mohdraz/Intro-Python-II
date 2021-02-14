# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, cr_room):
        self.name = name
        self.cr_room = cr_room
    def __str__(self):
        return "f from:player: {self.name} {self.cr_room} "