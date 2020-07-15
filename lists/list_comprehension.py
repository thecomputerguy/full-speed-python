#simple list comprehension with a for loop
simple = [element for element in [1,2,3,4,5,6]]
print(simple)
print()

#square of all the elements in the list
squared = [element * element for element in [1,2,3,4,5,6]]
print(squared)
print()

#even number squared
even_squared = [element * element for element in [1,2,3,4,5,6] if element % 2 == 0]
print(even_squared)
print()

#range squared without start and increment value
range_squared  = [element * element for element in range(10)]
print(range_squared)
print()

#range squared with start and increment value
range_squared_with_start_and_increment = [element * element for element in range(1,10,2)]
print(range_squared_with_start_and_increment)
print()

#get squared list between 1 to n
def get_squared_list(n):
    return [element * element for element in range(1,n+1)]

squared_list = get_squared_list(10)
print(squared_list)
print()

#create a list with cubes of first n numbers
def get_cubes(n):
    return [element * element * element for element in range(1,n+1)]

cubes = get_cubes(10)
print(cubes)
print()

#Alternate approach
def get_cubes_alternate_approach(n):
    return [element ** 3 for element in range(1,n+1)]

cubes_with_alternate_approach = get_cubes_alternate_approach(10)
print(cubes_with_alternate_approach)
print()

#list of even and odd numbers
def get_list_of_even_and_odd_numbers(n):
    even = [element for element in range(1,n+1) if element % 2 == 0]
    odd = [element for element in range(1,n+1) if element % 2 == 1]
    return [odd, even]

print(get_list_of_even_and_odd_numbers(21))
print()

#list of even and odd alternate solution
def get_even_odd(n):
    even = [element for element in range(1,n+1) if (element % 2) == 0]
    odd = [element for element in range(1, n+1) if element not in even]
    return [odd, even]

print(get_even_odd(21))
print()

#square of the even numbers
def get_list_of_square_of_even(n):
    return [element ** 2 for element in range(0, n) if (element % 2) == 0]

print(get_list_of_square_of_even(21))
print()

#square of the even numbers alternate solution
def get_list_of_square_of_even_alternate_solution(n):
    return [element * element for element in range(0,n+1, 2)]

print(get_list_of_square_of_even_alternate_solution(21))
print()

#create a list of square of even numbers which are not divisible by 3
def get_list_of_square_of_even_not_divisible_by_three(n):
    return [element*element for element in range(0,n+1) if (element %2 == 0 and element % 3 != 0)]

print(get_list_of_square_of_even_not_divisible_by_three(21))
print()

#create a list of square of even numbers which are not divisible by 3 alternate solution
def get_list_of_square_of_even_not_divisible_by_three_alternate_solution(n):
    return [element * element for element in range(0,n+1, 2) if (element % 3) != 0]

print(get_list_of_square_of_even_not_divisible_by_three_alternate_solution(21))
print()