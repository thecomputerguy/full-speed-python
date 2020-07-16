from Person import Person

class TenYearOld(Person):

    def __init__(self, name):
        Person.__init__(self, name, 10)

    def greet(self):
        print("I don't talk to strangers!")
    
ten1 = TenYearOld("Oly")
ten1.greet()




