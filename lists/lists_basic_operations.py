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

def get_sublist(list):
    return [list[0:3], list[3:]]

print(get_sublist([1,4,9,10,23]))