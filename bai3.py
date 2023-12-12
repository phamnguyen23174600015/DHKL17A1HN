def gia_tri(x, n):
    S =((x**2+1)*n)
    return(S)

x=float(input("x:"))
n=float(input("n:"))
S = gia_tri(x, n)
print("S=:", S)