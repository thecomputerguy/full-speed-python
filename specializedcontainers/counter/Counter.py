from collections import Counter
#print the counter
print(Counter('superfluous'))

#print the count of u
counter = Counter("superfluous")
print(counter['u'])
print()

#generates an iterable from string and then adds characters to list
print(list(Counter("code everyday").elements()))
print()

#most common characters in the string
print(Counter('practice or perish').most_common())
print()

#subtract
counter1 = Counter('eat drink code')
counter2 = Counter('exercise everyday')
print(counter1.subtract(counter2))
print()

print(counter1)