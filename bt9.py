so_nguyen_duong = int(input("Nhập một số nguyên dương: "))
while so_nguyen_duong <= 0:
    so_nguyen_duong = int(input("Nhập lại một số nguyên dương: "))
print("Countdown từ", so_nguyen_duong, "đến 1:")
while so_nguyen_duong >= 1:
    print(so_nguyen_duong)
    so_nguyen_duong -= 1
