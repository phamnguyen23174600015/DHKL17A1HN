a=float(input("nhâp số a:"))
b=float(input("nhập số b:"))
c=float(input("nhập số c:"))
p= (a+b+c)/2
dien_tich = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(f"Diện tích của tam giác là: {dien_tich}")
