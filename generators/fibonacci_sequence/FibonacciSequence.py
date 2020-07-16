def fibonacci_generator(n):
    result = []
    index = 0
    while index <= n:    
         if(index == 0 or index == 1):
             result.append(index)
             yield index
         else:
             result.append(result[index-1] + result[index-2])
             yield result[index]
         index = index+1

fib_gen = fibonacci_generator(8)
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print()

for seq in fibonacci_generator(8):
    print(seq)

print()

