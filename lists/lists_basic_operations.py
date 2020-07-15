#sublist
def sub_list(list):
    return list[1:3]    

result = sub_list([1,2,3,4,5])
print(result)

#concatenation
list1 = [1,2,4,5,6]
list2 = [5,6,7,8,9]
list3 = list1 + list2
print(list3)

#traverse
for element in list3:
    print(element)

#list slicing
def get_sublist(list):
    return [list[0:3], list[3:]]

print(get_sublist([1,4,9,10,23]))
print()

#append at the end
def append_to_end(list, num):
    list.append(num)
    return list

result = append_to_end([1,2,4,5,6], 10)
print(result)
print()

#average without using sum function
def get_average(list):
    sum = 0
    for element in list:
        sum += element
    return sum/len(list)

print(get_average([1,2,3,4,5,6]))
print()

#average with sum function
def get_average_with_sum_func(list):
    return sum(list)/len(list)

result = get_average_with_sum_func([1,2,3,4,5,6])
print(result)
print()

#remove from list
def remove_from_list(list, elements_to_remove):
    for element in elements_to_remove:
        list.remove(element)
    return list

result = remove_from_list([1,2,3,4,5,6,7,8],[5,8])
print(result)
print()