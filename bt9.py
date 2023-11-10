#gửi lãi
lai_suat = float(input("laĩ suất năm (%): "))
tien_gui = float(input("số tiền gửi (vnd): "))
thoi_gian = float(input("thời  gian gửi(tháng): "))
tien_lai= (tien_gui * thoi_gian * (lai_suat/100)) / 12
so_tien_nhan_duoc= tien_lai + tien_gui
print(f"tiền lãi = {tien_lai} vnd")
print(f"tổng số tiền nhận đượck = {so_tien_nhan_duoc} vnd")