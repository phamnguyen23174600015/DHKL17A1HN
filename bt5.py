nam = int(input("Nhập năm: "))
if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print(nam, "là năm nhuận.")
else:
    print(nam, "không là năm nhuận.")
