so_1=int(input("nhập số thứ 1: "))
so_2=int(input("nhập số thứ 2: "))
while so_2!=0:
    so_1, so_2 = so_2, so_1%so_2
print(f"UCLN là:", {so_1})


