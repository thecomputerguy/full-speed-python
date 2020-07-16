class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        #if x1 < x2 and y1 > y2:
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

        #else:
         #   print("Invalid coordinates.")

    def width(self):
        return self.x2 - self.x1

    def height(self):
        return self.y1 - self.y2

    def area(self):
        return self.width() * self.height()
    
    def perimeter(self):
        return (2 * self.width()) + (2 * self.height())

    def print_coordinates(self):
        print(self.x1, self.y1, self.x2, self.y2)

    def __str__(self):
        return (str(self.x1) + ", " + str(self.y1) + ", " + str(self.x2) + ", " + str(self.y2))
    
    def __repr__(self):
        return (str(self.x1) + ", " + str(self.y1) + ", " + str(self.x2) + ", " + str(self.y2))


class Square(Rectangle):
    
    def __init__(self, x1, y1, length):
        x2 = x1 + length
        y2 = y1 + length
        super().__init__(x1, y1, x2, y2)


square1 = Square(2, 7, 7)
print("Square Width " + str(square1.width()) + " Square area " + str(square1.area()))


rect1 = Rectangle(2, 7, 8, 4)
print(rect1)
rect1.print_coordinates()
print("width: " , rect1.width())
print("height: ", rect1.height())
print("Area: ", rect1.area())
print("perimeter: ", rect1.perimeter())
