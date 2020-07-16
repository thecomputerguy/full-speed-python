#reverse number generator
def reverse_generator(n):
    for element in range(n, -1, -1):
        yield element

rev_gen = reverse_generator(20)
print(next(rev_gen))
print(next(rev_gen))
print(next(rev_gen))
print(next(rev_gen))
print()

for element in reverse_generator(40):
    print(element)

print()
