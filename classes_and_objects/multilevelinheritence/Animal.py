class Animal():

    def __init__(self, name, food, characterstic):
        self.name = name
        self.food = food
        self.characterstic = characterstic

    def printer(self):
        print("I am a " + str(self.name) + ".")
    

class Mammal(Animal):
    
    def __init__(self, name, food):
        Animal.__init__(self, name, food, "warm blooded")
    
    def printer(self):
        print("I am warm blooded!")

class Carnivore(Mammal):

    def __init__(self, name):
        Mammal.__init__(self, name, "meat")
    
    def printer(self):
        print("I am a Lion!")

lion = Carnivore("simba")
lion.printer()

