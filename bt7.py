so_tien = int(input("Nhập số tiền cần đổi (VNĐ): "))
menh_gia = [500000, 200000, 100000, 50000]
for gia_tri in menh_gia:
    so_tong_tien = so_tien // gia_tri  
    so_tien %= gia_tri  
    print(f"Số tờ {gia_tri} VNĐ: {so_tong_tien}")
if so_tien > 0:
    print(f"Số tiền còn lại: {so_tien} VNĐ")