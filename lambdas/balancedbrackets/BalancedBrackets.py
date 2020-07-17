def isBalanced(brackets):
    count = 0
    for bracket in brackets:
        if bracket == "[":
            count +=1
        else:
            count -= 1
    return True if count == 0 else False

print("Are brackets balanced?")
print(isBalanced("[[[]]]"))
print()

print("Are brackets balanced?")
print(isBalanced("[[[]]"))
print()