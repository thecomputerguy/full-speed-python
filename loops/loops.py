#for loop in python
for item in [1,2,3,4,5,6,7,8,9]:
    print(item)
print()

#sum using loops
list = [5,6,7,8]
sum = 0
for item in list:
    sum += item

print(sum)
print()

#loops using range
for item in range(1,10):
    print(item)
print()

#Another way of iterating through the list using length and index
for index in range(len(list)):
    print(list[index])
print()

#looping using enumerate
for index, value in enumerate(list):
    print("index: ", index, "value: ", value)
print()

#looping through a string
for char in "full speed python":
    print(char)
print()

#while loop
n = 10
while n > 0:
    print(n)
    n = n-1
print()



