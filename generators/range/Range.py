#Generator with while loop
def range_generator(a, b):
    while a < b:
        yield a
        a = a+1

seq = range_generator(1,5)
print(next(seq))
print(next(seq))
print()

#Geenerator usage using a for loop
def range_with_for_loop_usage(a,b):
    while a < b:
        yield a
        a = a+1

#use the generator

for element in range_with_for_loop_usage(10,15):
    print(element)

print()

#Generate squares using generators
def squares(n):
    for element in range(n+1):
        yield element ** 2

square_generator = squares(20)
print(next(square_generator))
print(next(square_generator))
print(next(square_generator))
print(next(square_generator))
print(next(square_generator))
print()

for element in squares(10):
    print(element)

print()
