def calculator(operation, x, y):
    return operation(x, y)

result = calculator(lambda x,y: x+y, 10,20)
print("Addition:")
print(result)

result = calculator(lambda x,y: x/y, 20,10)
print("Division:")
print(result)
print()
