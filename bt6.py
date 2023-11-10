loai_xe=int(input("loại xe của bạn là: "))
so_km=float(input("số km đi được là "))
thoi_gian_cho= int(input("thời gian chờ; "))
if loai_xe==4:
    gia_mo_cua = 11000/0.8
    duoi_20km = 12100
    tren_20Km = 10000
else:
 gia_mo_cua = 13000/0.8
duoi_30km= 14100
tren_30km = 12000
if loai_xe ==4:
    if so_km <= 20:
        tien= gia_mo_cua + so_km * duoi_20km
    else:
        tien= gia_mo_cua + 20*duoi_20km + (so_km -20)*tren_20Km
else:
    if so_km <=30:
        tien= gia_mo_cua + so_km*duoi_30km
    else:
        tin= gia_mo_cua + 30*duoi_30km + (so_km -30)*tren_30km
phi_cho= max(0, thoi_gian_cho - 5)*800
tien_cuoc= tien + phi_cho
print("tiền chờ là:", phi_cho, "vnd") 
print("tiền di chuyển là:", tien, "vnd")
print("số tiền phải trả là:", tien_cuoc, "vnd")

    
