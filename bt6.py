#chia kẹo
keo_alice = int(input("số kẹo của alice: "))
keo_bod = int(input("số kẹo của bod: "))
keo_carole= int(input("số kẹo của carole: "))
tong_keo= keo_alice + keo_bod + keo_carole
so_keo_moi_nguoi= tong_keo // 3
so_keo_con_du= tong_keo % 3
print("tổng số kẹo:", tong_keo)
print("số kẹo mỗi người nhận được:", so_keo_moi_nguoi)
print("số kẹo dư:", so_keo_con_du)