import math
π = math.pi
print(π*2)
radius = float(input())
area = 1/2 * math.pi * math.pow(radius, 2)
area = round(area, 3)
print(f"The area of a circle with radius {radius} is {area}.")