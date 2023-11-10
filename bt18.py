x=int(input("nhập sô: "))
def kiem_tra_so_hoan_hao(num):
    tong = 0
    for i in range(1, num):
        if num % i == 0:
            tong += i
    return tong == num
if kiem_tra_so_hoan_hao(x):
    print(f"{x} là số hoàn hảo.")
else:
    print(f"{x} không phải là số hoàn hảo.")
