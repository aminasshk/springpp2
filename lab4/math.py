#1
import math
k=float(input("sandy engiz:"))
print("Radian:",math.radians(k))

#2
import math
h=float(input("Height:"))
a=float(input("Base,first value:"))
b=float(input("Base,second value:"))
print("Trapazoide area:",(a+b)*0.5*h)

#3
import math
n=int(input("Input number of sides: "))
s=float(input("Input the length of a side: "))
area=(n*s**2)/(4*math.tan(math.pi/n))
print("The area of the polygon is:", area)

#4
import math
b=int(input("a:"))
a=int(input("b:"))
print(float(a*b))
