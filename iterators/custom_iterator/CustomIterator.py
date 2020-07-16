class CustomIterator:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a < self.b:
            value = self.a
            self.a = self.a+1
            return value
        else:
            raise StopIteration
    
    def next(self):
        return self.__next__()
    
custom_range = CustomIterator(1,9)
print(custom_range.next())
print(custom_range.next())
print()

for element in CustomIterator(10,20):
    print(element)
print()