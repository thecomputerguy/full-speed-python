import math

def find_sin_cos_tan(x):
    sin = math.sin(x)
    cos = math.cos(x)
    tan = math.tan(x)
    return [sin,cos,tan]

print(find_sin_cos_tan(45))
