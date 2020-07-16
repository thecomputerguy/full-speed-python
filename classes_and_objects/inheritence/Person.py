class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello my name is %s" %self.name)

a = Person("Maria", 20)
b = Person("Alex", 21)

a.greet()
print()
b.greet()
print()

