

# Nhập số nguyên dương n từ người dùng
n = int(input("Nhập vào một số nguyên dương n: "))

# Biểu thức A: Tổng các số lẻ nhỏ hơn hay bằng n
a = sum([i for i in range(1, n + 1) if i % 2 != 0])

# Biểu thức B: Tổng các số chẵn nhỏ hơn hay bằng n
b = sum([i for i in range(1, n + 1) if i % 2 == 0])

# Biểu thức C: Tích các số từ 1 đến n
c = 1
for i in range(1, n + 1):
    c *= i

# Biểu thức D: Tích các số chia hết cho 3 nhỏ hơn hay bằng n
d = 1
for i in range(1, n + 1):
    if i % 3 == 0:
        d *= i

# Biểu thức E: Tổng các số nguyên tố nhỏ hơn hay bằng n
e = sum([i for i in range(1, n + 1) ])

# Biểu thức F: Tổng chuỗi đan dấu
f = sum([(-1)**i * i for i in range(1, n + 1)])

# Hiển thị kết quả
print(f"A = {a}")
print(f"B = {b}")
print(f"C = {c}")
print(f"D = {d}")
print(f"E = {e}")
print(f"F = {f}")
