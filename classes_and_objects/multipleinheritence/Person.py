class Person():

    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print("Hi, I am " + self.name + ".")
    
class Student(Person):

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        super().__init__(name)
    
    def report(self):
        print("My roll number is " + str(self.roll_no))

class Teacher(Person):

    def __init__(self, name, course):
        self.name = name
        self.course = course
        super().__init__(name)
    
    def introduce(self):
        print("I teach " + self.course + ".")

class TA(Student, Teacher):

    def __init__(self, name, roll_no, course, grade):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.grade = grade

    def details(self):
        if(self.grade == "A*" or self.grade == "A" or self.grade == "A-"):
            Person.greet(self)
            Teacher.introduce(self)
            Student.report(self)
            print("I got an " + self.grade + " in " + self.course)
        else:
            print(self.name + ", you can't apply for TAShip")

ta = TA("Ali", "13k-1234", "Data Structures", "A")
ta.details()
ta.greet()
ta.report()
ta.introduce()
print()

ta = TA("Ahmed", "14k-5678", "Algorithms", "B")
ta.details()
        

