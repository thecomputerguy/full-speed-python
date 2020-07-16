class EvenNumberIterator():

    def __init__(self, n):
        self.a = 0
        self.b = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a < self.b:
            value = self.a
            self.a += 2
            return value
        else:
            raise StopIteration

    def next(self):
        return self.__next__()

obj = EvenNumberIterator(10)
print(obj.next())
print(obj.next())
print()

for element in EvenNumberIterator(20):
    print(element)
print()