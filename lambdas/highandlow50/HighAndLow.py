#print the count of numbers greater than 50 or divisble by three as high
#the count of numbers less than or equal to 50 and not divisible by 3 as low
def highAndLowCount(nums):
    high = list(filter(lambda x:  x > 50 or x % 3 == 0, nums))
    low = list(filter(lambda x:  x <= 50 and not x % 3 == 0, nums))
    return [len(high), len(low)]

result = highAndLowCount([29,50,59,60,70,45,35,33,21,20,31])
print("high and low count:")
print(result)
print()
