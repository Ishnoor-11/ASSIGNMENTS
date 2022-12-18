import math
for item in range(0,346,15):
    a = math.sin(math.radians(item))
    b = math.cos(math.radians(item))
    print(item,"---",round( a,4), round (b,4))

