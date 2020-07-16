def odd_generator(n):
    for element in range(n+1):
        if element % 2 != 0:
            yield element
    
odd_gen = odd_generator(10)    
print(next(odd_gen))
print(next(odd_gen))
print(next(odd_gen))
print()

for odd_element in odd_generator(20):
    print(odd_element)

print()