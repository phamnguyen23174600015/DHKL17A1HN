def gia_tri(x, n):
    A=(x**2+n+1)**n +(x**2-n+1)**n
    return(A)

x=int(input("x:"))
n=int(input("n:"))
A= gia_tri(x,n)
print("A:", A)