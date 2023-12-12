Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cmath
>>> a=float(input("so a la:"))
so a la:1
>>> b=float(input("so b la:"))
so b la:3
>>> c=float(input("so a la:"))
so a la:4
>>> delta = (b**2) - (4*a*c)
>>> nghiem1 = (-b-cmath.sqrt(delta))/(2*a)
>>> nghiem2 = (-b+cmath.sqrt(delta))/(2*a)
>>> print("nghiem cua phuong trinh la:", nghiem1, nghiem2)
nghiem cua phuong trinh la: (-1.5-1.3228756555322954j) (-1.5+1.3228756555322954j)
