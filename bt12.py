so_nguyen = int(input("Nhập một số nguyên dương: "))
is_prime = True
if so_nguyen <= 1:
    is_prime = False
else:
    for i in range(2, int(so_nguyen**0.5) + 1):
        if so_nguyen % i == 0:
            is_prime = False
            break
if is_prime:
    print(so_nguyen, "là số nguyên tố.")
else:
    print(so_nguyen, "không là số nguyên tố.")
