so_kwh = float(input("Nhập số điện: "))
bac_1 = 50 * 1.678
bac_2 = 50 * 1.734
bac_3 = 100 * 2.014
bac_4 = 100 * 2.536
bac_5 = 100 * 2.834
bac_6 = (so_kwh - 300) * 2.927
tong_tien_dien = 0
if so_kwh <= 50:
    tong_tien_dien = so_kwh * 1.678
elif so_kwh <= 100:
    tong_tien_dien = bac_1 + (so_kwh - 50) * 1.734
elif so_kwh <= 200:
    tong_tien_dien = bac_1 + bac_2 + (so_kwh - 100) * 2.014
elif so_kwh <= 300:
    tong_tien_dien = bac_1 + bac_2 + bac_3 + (so_kwh - 200) * 2.536
elif so_kwh <= 400:
    tong_tien_dien = bac_1 + bac_2 + bac_3 + bac_4 + (so_kwh - 300) * 2.834
else:
    tong_tien_dien = bac_1 + bac_2 + bac_3 + bac_4 + bac_5 + bac_6
print("tiền điện:", tong_tien_dien, "vnd")
