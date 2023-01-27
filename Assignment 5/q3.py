import math

a = int(input("Enter side 1 of the triangle "))
b = int(input("Enter side 2 of the triangle "))
c = int(input("Enter side 3 of the triangle "))

s = (a+b+c)/2

x = math.sqrt (s*(s-a)*(s-b)*(s-c))
print ("Area of triangle is ",x)