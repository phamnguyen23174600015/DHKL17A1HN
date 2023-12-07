n = int(input("nhap so n:"))
if n <= 1:
    print(f"{n} ko la so hh")
else:
    tong = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            tong+= i
            if i != n // i:
                tong += n // i
    if tong== n:
        print(f"{n} la so hh.")
    else:
        print(f"{n} ko la so hh")