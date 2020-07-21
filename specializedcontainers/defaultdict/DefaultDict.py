
sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')
#regular dict
regular_dict = dict()
for word in words:
    if word in regular_dict:
        regular_dict[word] += 1
    else:
        regular_dict[word] = 1

print(regular_dict)
print()

#specialized dict 
from collections import defaultdict
default_dict = defaultdict(int)

for word in words:
    default_dict[word] += 1

print(default_dict)
print()
#one more example with account and balance
account_and_balance = [(1234, 100.23), (345, 10.45), (1234, 75.00),(345, 222.66), (678, 300.25), (1234, 35.67)]
#with regular dict
reg_dict = dict()
for account, balance in account_and_balance:
    if account in reg_dict:
        reg_dict[account].append(balance)
    else:
        reg_dict[account] = [balance]

print(reg_dict)
print()

#with default dict
def_dict = defaultdict(list)
for account, balance in account_and_balance:
    def_dict[account].append(balance)

print(def_dict)
print()

#key error if default factory is set to None
def_dict_with_none = defaultdict(None)

value = def_dict_with_none['mike']
print(value)