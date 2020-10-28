# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, list):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.list = list

    def printItems(self):
        output = f"{self.name} has\n"
        i = 0
        for item in self.list:
            output += " " + str(i+1) + ". " + item + "\n"
        return output

    def __str__(self):
        return f"Current Room: {self.name} \nDescription: {self.description} "
