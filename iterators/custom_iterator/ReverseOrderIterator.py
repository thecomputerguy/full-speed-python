class ReverseOrderIterator():

    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        list = []
        for element in range(self.n, -1, -1):
            list.append(element)
        
        return list
    
    def next(self):
        return self.__next__()
    

iter = ReverseOrderIterator(10)
print(iter.next())