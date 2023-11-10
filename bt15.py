tong=0
while True:
    so_nguyen = float(input("Nhập số (0 để dừng): "))
    if so_nguyen == 0:
        break
    tong += so_nguyen
print("Tổng các số nguyên đã nhập là:", tong)
