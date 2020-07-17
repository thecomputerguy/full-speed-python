def pairWithZeroSum(elements):
    for i in range(len(elements)):
        for j in range(i+1,len(elements)):
            sum_of_two_elements = elements[i] + elements[j]
            if sum_of_two_elements == 0:
                return True
            j = j+1
    return False

result = pairWithZeroSum([1,2,5,-5,6,-4,3,-8])
print("Pair exists?")
print(result)

result = pairWithZeroSum([1,2,5,6,8,9])
print("Pair exists?")
print(result)