gia_phong = [1260000, 1550000, 1830000, 1830000, 2120000, 2120000, 2540000, 4800000]
loai_phong = int(input("loại phòng: "))
so_dem = int(input("số đêm ở: "))
if 1 <= loai_phong <= 8:
    thanh_tien = gia_phong[loai_phong] * so_dem
    if 2 <= so_dem <= 3:
        thanh_tien *= 0.75  
    elif so_dem >= 4:
        thanh_tien *= 0.7  
    print(f"Thành tiền = {thanh_tien} vnđ")
else:
    print("Loại phòng không hợp lệ. Vui lòng chọn từ 1 đến 8.")
