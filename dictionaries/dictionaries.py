ages = {
    "Peter": 18,
    "Isabel": 19,
    "Anna": 20,
    "Thomas": 10,
    "Bob": 15,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10
}

#get Gabriel's age
print("Gabriel's age: ", ages["Gabriel"])
print()
#get everyone's age
for key,value in ages.items():
    print(key, " : ", value)
print()

#create a dictionary with curly braces
new_dict1 = {"Tiger": "Amazon"}
print(new_dict1["Tiger"])
print()

#create a dictionary with dict
new_dict2 = dict()
new_dict2["animal"] = "Elephant"
for key,value in new_dict2.items():
    print(key, " : ", value)
print()

#ordered dictionary: Mantains insertion order
from collections import OrderedDict #import ordered dictionary from collections
ordered_dict = OrderedDict()
ordered_dict["Facebook"] = "Top Tech"
ordered_dict["Amazon"] = "Top Tech"
ordered_dict["Google"] = "Dream"
ordered_dict["Netflix"] = "Super cool"

for ord_key, ord_val in ordered_dict.items():
    print(ord_key, " : ", ord_val)
print()

#dictionary keys other than strings
d = {
    0: [0,0,0],
    1: [1,1,1],
    2: [2,2,2]
}
print(d[2])
print()

#loop to get all keys
for age_key in ages:
    print(age_key, " : ", ages[age_key])

print()

#loop to get all keys and values using get method
for key in ages:
    print(key, " : ", ages.get(key))
print()

#loop to get all values
for key in ages:
    print(ages[key])
print()

#loop to get all values using values function
for value in ages.values():
    print(value)
print()

#loop to get both keys and values
for key, value in ages.items():
    print(key, " : ", value)
print()

#nested dictionaries
students = {
    "Peter": {"age" : 10, "address" : "Lisbon"},
    "Isabel": {"age": 15, "address" : "sesimbra"},
    "Anna": {"age": 9, "address" : "London"}
}
print(students)
print()
print(students["Peter"])
print()
print(students.get("Anna"))
print()

#looping through a nested dictionary
for person_id, person_info in students.items():
    print("Person name: ", person_id)
    for key in person_info:
        print(key, " : ", person_info[key])
    
print()

#dictionary size
def dictionary_size(students_dict):
    return 0 if students_dict == None else len(students_dict)
print(dictionary_size(students))
print() 

#Average of ages
def ages_average(ages):
    sum = 0
    for value in ages.values():
        sum += value
    avg = sum/len(ages)
    return avg
print(ages_average(ages))
print()

#using inbuilt sum function
ages_sum = sum(ages.values())
average_of_ages = ages_sum/len(ages)
print(average_of_ages)

#return the oldest student
def oldest_student(ages):
    max_value = next(iter(ages.values())) 
    max_value_key = 0
    for key, value in ages.items():
        if value > max_value: 
            max_value = value
            max_value_key = key
    return [max_value_key, max_value]
print(oldest_student(ages))
print()

#Alternate solution to find the oldest student
def oldest_student_alternate_solution(ages):
    keys = list(ages.keys())
    values = list(ages.values())
    key = keys[values.index(max(values))]
    return [key, ages[key]]

print(oldest_student_alternate_solution(ages))
print()

#increment age of each student by n
def update_ages(ages, n):
    for key,value in ages.items():
        ages[key] = value + n
    return ages

print(update_ages(ages, 5))
print()

#size of a dictionary
def size_of_dictionary(ages):
    return len(ages)
print(size_of_dictionary(ages))
print()

#size of a dictionary alternate solution
def size_of_dictionary_alternate(ages):
    return len(ages.keys())
print(size_of_dictionary_alternate(ages))
print()

#average of student ages in a nested dictionary
def average_in_nested_dictionary(students):
    age_sum = 0
    for key in students.keys():
        student = students[key]
        student_age = student["age"]
        age_sum += student_age
    return age_sum/len(students)
print(average_in_nested_dictionary(students))
print()

#average of student ages in a nested dictionary
def average_in_nested_dictionary_alternate_solution(students):
    age_sum = 0
    for value in students.values():
        age_sum += value["age"]
    return age_sum/len(students)

print(average_in_nested_dictionary_alternate_solution(students))
print()

#find students living in a particular area
def find_students_by_address(students, address):
    students_list = []
    for name, info in students.items():
        if info["address"] == address:
            students_list.append(name)
    return sorted(students_list)

print(find_students_by_address(students, "Lisbon"))
print()