class FibonacciIterator():

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self
    
    def __next__(self):
        result = []
        for index in range(self.n):
            if index == 0 or index == 1:
                result.append(index)
            else:
                result.append(result[index-1] + result[index-2])
        return result
    
    def next(self):
        return self.__next__()

fib_iterator = FibonacciIterator(8)
print(fib_iterator.next())
print()


                
