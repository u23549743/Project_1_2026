from cmath import sqrt
import math

#b = 100
#c= 2
#x = 3
#a = b*x+c
#print(a)

#y =b**2-(4*a*c)
#print(y)
#p =sqrt(b**2-(4*a*c))
#print(p)

#l = math.sqrt(b**2-(4*a*c))
#print(l)

a = input("Enter a value for a: ")
b = input("Enter a value for b: ")
c = input("Enter a value for c: ")

a = float(a)
b = float(b)
c = float(c)
l = math.sqrt(b**2-(4*a*c))
print(l)