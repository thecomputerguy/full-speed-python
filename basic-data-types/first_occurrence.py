def first_occurrence(s):
    a = s.find("b")
    b = s.find("ccc")
    return [a,b]

[a,b] = first_occurrence("aaabbbccc")
print(a)
print(b)