import math

def find_maximum(x,y):
    return max(x,y)

print(find_maximum(10,20))

def find_maximum_using_if_else(x,y):
    if x > y:
        return x
    else:
        return y

print(find_maximum(20,30))