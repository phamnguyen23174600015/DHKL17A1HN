try:
    a, b, c = map(float, input("Nhap 3 canh cua tam giac: ").split())
    if a <= 0  or b <= 0 or c <= 0:
        raise ValueError("độ dài cạnh không hợp lí: ")
    if a <= 0 or b <= 0 or c <=0 or a + b <= c or b + c <= a or a + c <= b:
        raise ValueError("không là tam giác: ")
except  ValueError as e:
    print("lỗi thử lại sau")
else:
    print("ba cạnh đúng là cạnh của tam giác")
