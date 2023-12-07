x = int(input("Nhap vao so nguyen duong x: "))
if x < 2:
    print(f"{x} False")
else:
    for i in range(2,x):
        if x%i == 0:
            print(f"{x} False")
            break
    else:
        print(f"{x} True")