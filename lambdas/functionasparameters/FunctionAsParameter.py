def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def divide(x, y):
    return x/y

def multiply(x, y):
    return x*y

def calculator(operation, x, y):
    return operation(x, y)

print("Addition of two numbers")
result = calculator(add,10,20)
print(result)
print()

print("Subtraction of two numbers")
result = calculator(subtract, 20, 10)
print(result)
print()






