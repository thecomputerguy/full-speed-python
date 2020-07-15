def transform_string(s):
    s = s[:1] + s[0] + s[1:]
    s = s[:1] + s[0] + s[1:]
    s = s[:3] + s[3] + s[3:]
    s = s[:3] + s[3] + s[3:]
    s = s[:6] + s[6] + s[6:]
    s = s[:6] + s[6] + s[6:]
    print(s)

transform_string("abc")

