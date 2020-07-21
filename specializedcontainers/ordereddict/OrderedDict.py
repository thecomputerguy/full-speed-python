#getting the sorted keys from the normal dictionary
normal_dict = {"apple":10, 'pear': 50, 'orange': 56, 'banana': 66}
print(normal_dict)
print()

#unsorted keys pulled from normal_dict
for key in normal_dict.keys():
    print(key, normal_dict[key])
print()
print()

#get the keys from normal dict and sort
keys = normal_dict.keys()
sortedKeys = sorted(keys)
print(sortedKeys)
print()



#getting the sorted keys from an ordereddict
from collections import OrderedDict
print(normal_dict)
ordered_dict = OrderedDict(sorted(normal_dict.items()))
print(ordered_dict)
print()

#keys are in sorted order in ordereddict
for key in ordered_dict.keys():
    print(key, ordered_dict[key])
print()
print()
