#bt4
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Diện tích tam giác: ", S)
