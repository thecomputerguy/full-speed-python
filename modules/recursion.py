def factorial(n):
    if(n <= 1): return 1
    return n * factorial(n-1)

print(factorial(5))

def fibonacci(n):
    if(n <= 1): return n
    return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(7))

def sum_n_numbers(n):
    if n <= 1: return n
    return n + sum_n_numbers(n-1)

print(sum_n_numbers(5))