so_1 = int(input("số thứ 1: "))
so_2 = int(input("số thứ 2: "))
def bcnn(a, b):
    def ucln(x, y):
        while y != 0:
            x, y = y, x % y
        return x
    return abs(a * b) // ucln(a, b)
bcnn = bcnn(so_1, so_2)
print(f"bcnn là: {bcnn}")