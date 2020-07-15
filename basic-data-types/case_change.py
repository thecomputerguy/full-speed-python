def case_change(s):
    a = s.upper()
    b = s.lower()
    return [a,b]

[a,b] = case_change("varuN Sharma")
print(a, b)