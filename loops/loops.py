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

#sum list function
def sum_list(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

sum_of_list = sum_list([1,2,4,5,6,7,8])
print(sum_of_list)
print()

#find the maximum from the list
def find_maximum(nums):
    max = nums[0]
    for index in range(1, len(nums)):
        if(nums[index] > max):
            max = nums[index]
    
    return max
print(find_maximum([1,2,3,4,5,6,7,8,9]))

#find maximum alternate solution
import math
def find_maximum_alternate(nums):
    current_max = 0
    for element in nums:
        current_max = max(current_max, element)
    return current_max

print(find_maximum_alternate([1,2,3,4,5,6,7,8,9]))
print()

#find the maximum value index
def find_maximum_value_index(nums):
    current_max = nums[0]
    current_max_index = 0
    for index,value in enumerate(nums):
        if(value > current_max):
            current_max = value
            current_max_index = index

    return [current_max_index,current_max]

print(find_maximum_value_index([1,2,3,4,5,6,7,8,9,10,11]))
print()

#reverse a list
def reverse(nums):
    size = len(nums)
    reversedList = []
    for index in range(size-1, -1, -1):
        reversedList.append(nums[index])
    return reversedList
print(reverse([1,2,3,4,5,6,7,8,9]))
print()

#revers a list alternate solution
def reverse_alternate(nums):
    size = len(nums)
    reversedList = []
    for index in reversed(range(size)):
        reversedList.append(nums[index])
    return reversedList

print(reverse_alternate([1,2,3,4,5,6,7,8,9]))
print()

#reverse a list one more alternative
def reverse_alternate_second(nums):
    size = len(nums)
    reversedList = [None]*size
    length = size
    for item in nums:
        length = length - 1
        reversedList[length] = item
    return reversedList

print(reverse_alternate_second([1,2,3,4,5,6,7,8,9]))

#list is sorted in given order or not
def is_sorted(nums, order = "asc"):
    if order == "asc":
        for index in range(1,len(nums)):
            if nums[index] < nums[index-1]:
                 return False
    elif order == "desc":
        for index in range(1, len(nums)):
            if nums[index] > nums[index-1]:
                 return False
    else:
        raise Exception("invalid order: order must be either {} or {}".format("asc", "desc"))

    return True

print(is_sorted([1,2,3,4,5,6,7,8,9], "asc"))
print(is_sorted([1,2,3,4,8,5,9,6,7], "asc"))
print(is_sorted([9,8,7,6,5,4,3,2,1], "desc"))
print(is_sorted([9,8,7,6,5,3,4,2,1], "desc"))
print()

#list has duplicates or not brute force solution
def has_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                 return True
    return False

print(has_duplicate([1,2,3,4,5,6,7,8,9]))
print(has_duplicate([1,2,2,3,3,4,5,6,8,8]))
print()

#print even/odd in descending order
def print_even_odd(num):
    for element in range(num, -1, -1):
        if element % 2 == 0:
            print("even: ", element)
        else:
            print("odd: ", element)

print_even_odd(10)
print()