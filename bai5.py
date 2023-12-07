import math
n=float(input("so n la:"))
x=float(input("so x la:"))
A=math.pow((math.pow(x, 2) + 1 + x), n) + math.pow((math.pow(x, 2) + 1 - x), n)
print("A=",A)